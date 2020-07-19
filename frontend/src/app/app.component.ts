import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'hello there';
  images = [
    'http://localhost:5000/assets/images/kopek.jpg',
    'http://localhost:5000/assets/images/Scarlet_Macaw.jpg'
  ];
}
