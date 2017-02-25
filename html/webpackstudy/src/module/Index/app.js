/*
 * @Author: Leon
 * @Date: 2017-02-03 14:02:39
 * @Last Modified by: Leon
 * @Last Modified time: 2017-02-04 09:51:44
 */

import App from './app.vue'
import Vue from 'vue'

new Vue({ // eslint-disable-line no-new
  el: '#app',
  render: page => page(App),
  http: {
    header: {
      'Content-Type': 'application/json'
    }
  }
})
