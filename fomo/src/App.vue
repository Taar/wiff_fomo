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
      <h3>You missed out on these films</h3>
      <ul id="missed-films" class="films">
        <li v-for="film in missedFilms" class="film missed">
          <film v-bind:film="film"></film>
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
import moment from 'moment';
import momentTimezones from 'moment-timezones';

export default {
  name: 'app',
  components: { Collisions, Film },
  data () {
    let timezone = 'US/Eastern';
    let films = [];
    let missedFilms = [];
    let currentDate = moment().tz(timezone);
    for (let film of json) {
      let startDate = moment(film.start_time).tz(timezone);
      if (startDate > currentDate) {
        films.push(film);
      } else {
        missedFilms.push(film);
      }
    }
    return {
      films: films,
      missedFilms: missedFilms
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
.missed {
}
</style>
