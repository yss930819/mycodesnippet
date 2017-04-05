<template>
  <div class="content-wrapper">
     <my-navbar></my-navbar>
      <div class="btn btn-danger">
       1
      </div>
  </div>
 
</template>

<script>
import navbar from 'components/Navbar/navbar.vue'

export default {
  name: 'form',
  components:{
    'my-navbar':navbar,
  }
}
</script>

<style>
  .content-wrapper {
    box-sizing: border-box;
    min-height: 100%;
}
</style>

