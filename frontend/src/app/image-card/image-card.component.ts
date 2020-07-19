import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'image-card',
  templateUrl: './image-card.component.html',
  styleUrls: ['./image-card.component.scss']
})
export class ImageCardComponent implements OnInit {

  @Input() image = '';

  liked = false;

  constructor() { }

  ngOnInit(): void {
  }

  like() {
    this.liked = !this.liked;
  }

}
