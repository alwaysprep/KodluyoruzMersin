import { Component, OnInit } from '@angular/core';
import { map } from 'rxjs/operators';
import { AngularFirestore } from '@angular/fire/firestore';

import { ImageType } from '../image';


@Component({
  selector: 'image-list',
  templateUrl: './image-list.component.html',
  styleUrls: ['./image-list.component.scss']
})
export class ImageListComponent implements OnInit {

  constructor(
    private firestore: AngularFirestore
  ) { }

  images;

  ngOnInit(): void {
    this.images = this.firestore.collection('images').snapshotChanges()
      .pipe(
        map(actions => actions.map(a => {
          const data = a.payload.doc.data() as ImageType;
          const id = a.payload.doc.id;
          return { id, ...data };
        }))
      );
  }

}
