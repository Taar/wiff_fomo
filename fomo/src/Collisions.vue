<template>
  <div>
    <button class="white-background" v-on:click="show = !show">What I'm missing out on ...</button>
    <transition name="fade">
      <div v-if="film.collisions.length">
        <ul v-if="show" class="films border">
          <li class="item" v-for="c_film in film.collisions">
            <film v-bind:film="c_film"></film>
          </li>
        </ul>
      </div>
      <div v-else>
        <div v-if="show" class="films border">
          <p>Relax! You're not going to miss anything! :)</p>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import Film from './Film.vue';

export default {
  name: 'collisions',
  components: { Film },
  props: ['film'],
  data () {
    return {
      show: false
    }
  },
  methods: {
  }
}
</script>

<style>
.border {
  -moz-border-radius: 15px;
  border-radius: 15px;
  border: 1px solid #000;
  padding: 5px;
  background-color: #fff;
}
.item {
  border-bottom: 1px dashed #000;
}
.films {
  list-style: none;
  margin: 0px;
}
.white-background {
  background-color: #fff;
}
</style>
