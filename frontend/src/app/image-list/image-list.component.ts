import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'image-list',
  templateUrl: './image-list.component.html',
  styleUrls: ['./image-list.component.scss']
})
export class ImageListComponent implements OnInit {

  images = [
    'http://localhost:5000/assets/images/kopek.jpg',
    'http://localhost:5000/assets/images/Scarlet_Macaw.jpg'
  ];

  constructor() { }

  ngOnInit(): void {
  }

}
