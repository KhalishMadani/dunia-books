<template>
  <main class="main-page">
    <h1>Library</h1>
    <ul v-for="(item, index) in respon" :key="item.id">
      <li>{{ index+1 }} {{ item.book_name }} - <a :href="backendUrl + item.book" target="_blank">Download PDF</a>, {{ item.created_at }}</li>
    </ul>
  </main>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';

const backendUrl = ref('http://127.0.0.1:8000/')
const respon = ref([])
const library = ref([
  {
    id:1,
    name: 'Yupi',
    category: 'Gum'
  },
  {
    id:2,
    name: 'Snickers',
    category: 'Snack'
  }
])

console.log(library)

onMounted( async() => {
  console.log('mounted!!')
  try {
    const response = await axios.get("library/")
    respon.value = response.data.data
    console.log(respon)
  } catch(err) {
    console.log("api error: ", err)
  }
})
</script>