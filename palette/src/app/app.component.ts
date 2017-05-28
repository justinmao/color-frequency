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

  constructor(private appService: AppService) { }

  ngOnInit() {
    this.getPalette(this.imageUrl);
    // this.makePaletteRequest(this.imageUrl).subscribe(centroids => {
    //   this.centroids = centroids;
    // });
    console.log(this.centroids);
  }

  getPalette(imageUrl) {
    this.appService.makePaletteRequest(imageUrl).subscribe(centroids => {
      this.centroids = centroids.centroids;
    })
  }



}
