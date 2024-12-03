<template>
  <div>
    <h1>{{ blog.title }}</h1>
    <img :src="blog.main_image" alt="Blog Image" style="max-width: 100%" />
    <p>{{ blog.description }}</p>

    <h2>Comments</h2>
    <CommentList :blogId="blog.id" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import CommentList from './CommentList.vue';

const route = useRoute();
const blog = ref({});

onMounted(async () => {
  const response = await axios.get(`/api/blogs/${route.params.id}/`);
  blog.value = response.data;
});
</script>
