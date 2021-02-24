import { Component, OnInit } from '@angular/core';
import { products } from '../products';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent{
  products = products;
  constructor() { }
  // tslint:disable-next-line:typedef
  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }
}
