import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'image-list',
  templateUrl: './image-list.component.html',
  styleUrls: ['./image-list.component.scss']
})
export class ImageListComponent implements OnInit {

  constructor(private http: HttpClient) { }

  images;

  ngOnInit(): void {
    this.images = this.http.get('http://localhost:5000/get_images_list');
  }


}
