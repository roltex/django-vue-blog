<template>
  <div>
    <ul>
      <li v-for="comment in comments" :key="comment.id">
        <p>{{ comment.content }}</p>
        <small>By {{ comment.author.username }}</small>
      </li>
    </ul>
    <CommentForm :blogId="blogId" @commentAdded="fetchComments" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import CommentForm from './CommentForm.vue';

const comments = ref([]);
const blogId = defineProps(['blogId']);

const fetchComments = async () => {
  const response = await axios.get(`/api/blogs/${blogId}/comments/`);
  comments.value = response.data;
};

onMounted(fetchComments);
</script>
