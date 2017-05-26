var express = require('express');
var Canvas = require('canvas');
var Image = Canvas.Image;
var router = express.Router();
var request = require('request').defaults({ encoding: null });

router.route('/image')
  .post(function(req, res) {
    var url = req.body.url;
    request(url, function(error, response, body) {
      var img = new Image();
      img.onload = function() {
        var centroids = analyze(img, 3);  // 3 color placeholder
        res.json({
          centroids: centroids
        });
      };
      img.src = new Buffer(body, 'binary');
    });

  });


// K-means cluster analysis adapted from https://dstein64.github.io/k-means-quantization-js/
// with references from https://miguelmota.com/blog/k-means-clustering-in-javascript/
// and http://burakkanber.com/blog/machine-learning-k-means-clustering-in-javascript-part-1/

function arraysEqual(a1, a2) {
  if (a1.length !== a2.length) return false;
  for (var i = 0; i < a1.length; ++i) {
    if (a1[i] !== a2[i]) return false;
  }
  return true;
}

function kmeans(data, k) {

  // Initialize k cluster centroids
  var centroids = [];
  for (var c = 0; c < k; ++c) {
    var idx = Math.floor(Math.random() * data.length);
    centroids.push(data[idx])
  }

  while (true) {
    var clusters = [];
    for (var c = 0; c < k; ++c) {
      clusters.push([]);
    }
    // Assign each data point to its closest cluster centroid
    for (var i = 0; i < data.length; ++i) {
      var minimumDistance = Infinity;
      var closestCentroid = -1;
      for (var c = 0; c < centroids.length; ++c) {
        var distance = 0;
        if (c < centroids.length) {
          for (var d = 0; d < data[i].length; ++d) {
            distance += Math.pow(data[i][d] - centroids[c][d], 2);
          }
          if (distance < minimumDistance) {
            minimumDistance = distance;
            closestCentroid = c;
          }
        }
      }
      clusters[closestCentroid].push(data[i]);
    }

    // Move each cluster centroid to the average position of its data points
    var converged = true;
    for (var c = 0; c < k; ++c) {
      var centroid = [];
      if (clusters[c].length > 0) {
        if (clusters[c].length === 0) return [];
        var runningCentroid = [];
        for (var i = 0; i < clusters[c][0].length; ++i) {
          runningCentroid.push(0);
        }
        for (var i = 0; i < clusters[c].length; ++i) {
          var point = clusters[c][i];
          for (var j = 0; j < point.length; ++j) {
            runningCentroid[j] += (point[j] - runningCentroid[j]) / (i+1);
          }
        }
        centroid = runningCentroid;
      } else {
        var idx = Math.floor(Math.random() * data.length);
        centroid = data[idx];
      }
      converged = converged && arraysEqual(centroid, centroids[c]);
      centroids[c] = centroid;
    }
    if (converged) break;
  }
  return centroids;

}

function analyze(image, k) {
  // Reduce image size for faster processing (at the cost of accuracy)
  var cvs = new Canvas(150, 150);
  var context = cvs.getContext("2d");
  context.drawImage(image, 0, 0, 150, 150);
  var flatData = context.getImageData(0, 0, 150, 150).data;
  var channels = flatData.length / (cvs.width * cvs.height)
  var data = [];
  for (var i = 0; i < flatData.length; i+= channels) {
    data.push(flatData.slice(i, i + channels));
  }
  return kmeans(data, k);
}

module.exports = router;
