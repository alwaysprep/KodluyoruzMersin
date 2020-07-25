import { Component, OnInit, Input } from '@angular/core';
import { AngularFirestore } from '@angular/fire/firestore';


@Component({
  selector: 'image-card',
  templateUrl: './image-card.component.html',
  styleUrls: ['./image-card.component.scss']
})
export class ImageCardComponent implements OnInit {

  @Input() id = '';
  @Input() image = '';
  @Input() liked = false;
  @Input() description = '';

  imageDoc;

  constructor(private afs: AngularFirestore) { }

  ngOnInit(): void {
    this.imageDoc = this.afs.doc('/images/' + this.id);
  }

  like() {
    this.liked = !this.liked;
    this.imageDoc.update({ 'like': this.liked });

  }

}
