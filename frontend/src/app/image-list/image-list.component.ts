import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'image-list',
  templateUrl: './image-list.component.html',
  styleUrls: ['./image-list.component.scss']
})
export class ImageListComponent implements OnInit {

  constructor(private http: HttpClient) { }

  images = [
    'http://localhost:5000/assets/images/kopek.jpg',
    'http://localhost:5000/assets/images/Scarlet_Macaw.jpg'
  ];

  ngOnInit(): void {
    this.http.get('http://localhost:5000/get_images_list')
      .subscribe(this.printResults);
  }

  printResults(data) {
    this.images = data;
    console.log(this.images);
  }

}
