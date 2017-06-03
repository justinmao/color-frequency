import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import 'rxjs/add/operator/map'

@Injectable()
export class AppService {

  constructor(private http: Http) { }

  makePaletteRequest(imageUrl, k) {
    var request = {
      'url': imageUrl,
      'k': k
    }
    return this.http.post('/api/image', request)
      .map((response: Response) => response.json());
  }

}
