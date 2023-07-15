import '../scss/app.scss';
import 'bootstrap/dist/css/bootstrap.min.css';

import Axios from 'axios';
import Vue from 'vue';


window.axios = Axios;

window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

let token = document.head.querySelector('meta[name="csrf_token"]');

if (token) {
    window.axios.defaults.headers.common['X-CSRFToken'] = token.content;
} else {
    console.error('CSRF token not found');
}

window.Vue = Vue;
