import {Component, Input, OnInit} from '@angular/core';
import { products } from '../products';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})

export class ProductItemComponent{
  products = products;
  // @ts-ignore
  @Input categoryId: number;

  // tslint:disable-next-line:typedef
  remove(product: any) {
    product.show = false;
    // products.splice(product.id - 1, 1);
  }

  // tslint:disable-next-line:typedef
  like(product: any) {
    product.likes += 1;
  }

  constructor() { }
  // // tslint:disable-next-line:typedef
  // onNotify() {
  //   window.alert('You will be notified when the product goes on sale');
  // }
}
