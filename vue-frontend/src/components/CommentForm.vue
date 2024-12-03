<template>
  <form @submit.prevent="submitComment">
    <textarea v-model="content" placeholder="Write a comment"></textarea>
    <button type="submit">Submit</button>
  </form>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const content = ref('');
const blogId = defineProps(['blogId']);

const submitComment = async () => {
  await axios.post(`/api/blogs/${blogId}/comments/`, { content: content.value });
  content.value = '';
  $emit('commentAdded');
};
</script>
