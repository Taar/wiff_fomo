<template>
  <div>
    <strong>{{ film.Title }}</strong>
    <span>&nbsp;-&nbsp;</span>
    <span class="date">{{ film.Date }}</span>
    &nbsp;<span class="label">starts:</span>&nbsp;<span class="start">{{ film['Start Time'] }}</span>
    &nbsp;<span class="label">ends:</span>&nbsp;<span class="end">{{ film['End Time'] }}</span>
    &nbsp;<span class="at">@</span><span class="place">{{ film['Venue'] }}</span>
  </div>
</template>

<script>

export default {
  name: 'film',
  props: ['film'],
  data () {
    return { }
  }
}
</script>

<style>
.date {
  color: #1891ba;
  font-weight: bold;
}
.end {
  color: #ba4618;
  font-weight: bold;
}
.start {
  color: #18ba40;
  font-weight: bold;
}
.label {
  font-style: italic;
  font-weight: bold;
}
.at {
  color: #8e18ba;
  font-weight: bold;
  font-size: .8em;
}
.place {
  font-weight: bold;
  font-size: .8em;
}
</style>
