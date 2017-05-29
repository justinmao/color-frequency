import { Component, OnInit } from '@angular/core';

import { AppService } from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'app works!';
  imageUrl = 'http://www.fnordware.com/superpng/pnggrad16rgb.png';
  centroids: any = [];
  colors: any = [];

  // public doughnutChartLabels:string[] = ['Download Sales', 'In-Store Sales', 'Mail-Order Sales'];
  // public doughnutChartData:number[] = [350, 450, 100];
  // public doughnutChartType:string = 'doughnut';
  //
  // public chartClicked(e:any):void {
  //   console.log(e);
  // }
  //
  // public chartHovered(e:any):void {
  //   console.log(e);
  // }

  constructor(private appService: AppService) { }

  ngOnInit() {
  }

  analyze() {
    this.colors = [];
    this.getPalette();
    for (var i = 0; i < this.centroids.length; ++i) {
      var centroid = this.centroids[i];
      var r = Math.floor(centroid[0]);
      var g = Math.floor(centroid[1]);
      var b = Math.floor(centroid[2]);
      var a = Math.round(centroid[3]/255 * 10)/10;
      this.colors.push("rgba(" + r + ", " + g + ", " + b + ", " + a + ")");
    }
  }
  getPalette() {
    this.appService.makePaletteRequest(this.imageUrl).subscribe(centroids => {
      this.centroids = centroids.centroids;
    })
  }

}
