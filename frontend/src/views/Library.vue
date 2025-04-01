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

    <!-- <div class="">
      <embed :src="pdfs" style="width: 100vh; height: 100vh;">
    </div> -->
  </main>
</template>

<script setup>
import { ref, onMounted, computed, inject } from 'vue';
import pdf from "../assets/MUHAMMAD_KHALISH_MADANI.pdf"

// const pdfs = ref(pdf)
const pdfs = "http://127.0.0.1:8000/media/pdfs/two_scoops_of_django.pdf"

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
