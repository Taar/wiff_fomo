<template>
  <div id="app" class="container">
    <div class="row">
      <h1 class="name">WIFF FoMO</h1>
      <ul id="films" class="films">
        <li v-for="film in films" class="film">
          <film v-bind:film="film"></film>
          <collisions v-bind:film="film"></collisions>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
let normalize = require('./assets/css/normalize.css');
let skeleton = require('./assets/css/skeleton.css');
let json = require('json!./assets/test.json');

import Collisions from './Collisions.vue';
import Film from './Film.vue';

export default {
  name: 'app',
  components: { Collisions, Film },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      films: json
    }
  },
  methods: {
  }
}
</script>

<style>
.name {
  text-align: center;
}
.films {
  list-style: none;
}
.film {
  -moz-border-radius: 15px;
  border-radius: 15px;
  background-color: #ededed;
  padding: 5px;
}
</style>
