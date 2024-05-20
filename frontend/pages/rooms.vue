<template>
    <div>
        <input v-model="room"/>
        <button @click="join()">join</button>
    </div>
</template>
<script setup>
    const room = ref('')
    async function join(){
        await $fetch(`http://127.0.0.1:8000/chat/${room.value}/join_self/`,{
            method: 'PUT',
            credentials: 'include',
            headers:{
                'Accept': 'application/json'
            }
        })
    }
</script>
<style lang="">
    
</style>