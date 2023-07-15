<template>
  <div class="alert-notification" :class="{ 'alert-notification__active': show }">
    <p>Saved successfully</p>
  </div>
</template>

<script>
export default {
  name: 'Notification',
  props: {
    show: false
  },
}
</script>

<style lang="scss">
@import 'resources/scss/variables.scss';

.alert-notification {
  background: #cfffc8;
  border-radius: 4px;
  border: solid 2px #bdfbb4;
  color: #2d2d2d;
  font-weight: bold;
  position: fixed;
  padding: 15px 20px;
  top: 10px;
  left: 10px;
  transform: translateX(-150%);
  transition: all 0.3s ease-in-out;

  &__active {
    transform: translateX(0%);
  }
}

</style>
