<template>
  <div class="home-page">
    <h1 class="display-5 fw-bold text-center">
      Zones and Distributions
    </h1>

    <div class="col-lg-6 mx-auto zones mb">
      <zone-editable
        v-for="zone in zones"
        :id="zone.id"
        :name="zone.name"
        :distributions="zone.distributions"
        :key="zone.uid"
        @edit="zone.name = $event.name"
        class="zone"
      />
    </div>

    <h1 class="display-5 fw-bold text-center">
      To Do List
    </h1>

    <ul class="col-lg-6 mx-auto">
      <li>Add the percentage symbol to each distribution number while is not being edited</li>
      <li>The cancel button is not working</li>
      <li>Without refreshing the page, be able to edit all the distributions from a zone</li>
      <li>Be able to add more distributions</li>
      <li>Be able to remove distributions</li>
      <li>When the user is not able to save due to some error, the error must be showed</li>
      <li>The sum of all distributions must be ensured to be 100% in anyway</li>
      <li>The distributions must be integer</li>
      <li>The zone name cannot be empty</li>
      <li>The zone name cannot have more than one space between each word</li>
      <li>The zone name cannot have spaces at start or the end</li>
      <li>The zone name cannot be repeated in any way</li>
      <li>Create a new field "updated_at" that is going to store the date when the name field change</li>
      <li>Show the updated_at field value near each zone name</li>
      <li>Add a way for the user to know that an element is being saved</li>
      <li>When the number of distributions is 5 or greater, the background of that zone must change to any color while is not being edited</li>
    </ul>
  </div>
</template>

<script>
import ZoneEditable from './ZoneEditable.vue';

export default {
  name: 'HomePage',
  components: {
    ZoneEditable
  },
  props: {
    context: {
      type: Object
    }
  },
  data() {
    return {
      zones: [],
      zoneUid: 0
    };
  },
  mounted() {
    this.zones = this.context.zones.map(data => {
      return {
        id: data.id,
        name: data.name,
        uid: this.zoneUid++,
        distributions: data.distributions
      };
    });
  }
}
</script>

<style lang="scss">
@import 'resources/scss/variables.scss';

.home-page {
  .zones {
    display: flex;
    gap: 4px;
    flex-direction: column;
  }
}
</style>
