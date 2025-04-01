<template>
  <main class="main-page">
    <h1>Library</h1>
    <div class="home-page">
      <input v-model="searchBook" type="text" class="form-control" placeholder="--Search Book--">
    </div>
    <ul v-for="(item, index) in filterBooks" :key="item.id">
      <li>{{ index+1 }}. {{ item.book_name }} - <a :href="item.book">Open</a></li>
    </ul>

    <canvas id="pdf-canvas">

    </canvas>
  </main>
</template>

<script setup>
import { ref, onMounted, computed, inject } from 'vue';

const api = inject('api')
const libraries = ref([])

onMounted( async() => {
  console.log('mounted!!')
  try {
    const response = await api.get("library/")
    libraries.value = response.data.data
    console.log(libraries)
  } catch(err) {
    console.log("api error: ", err)
  }
})

const searchBook = ref("")
const filterBooks = computed(() => {
  return libraries.value.filter( (item) =>
  item.book_name.toLowerCase().includes(searchBook.value.toLowerCase())
  )
})

const selectedPDF = ref(null)
const loadPDF = async (pdfPath) => {
  try {
    const response = await api.get(pdfPath, {responseType:'blob'})
    const url = window.URL.createObjectURL(new Blob([response.data]))
    selectedPDF.value = url;
  } catch (err) {
    console.log('pdf load error: ', err)
  }
}
</script>

<style>
.home-page {
  margin-top: 1rem;
  margin-bottom: 1rem;

  input{
    text-align: center;
  }
}
</style>
