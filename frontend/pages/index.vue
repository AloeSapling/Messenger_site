<template>
    <div>
        <p>Hello world</p>
        <button @click="get_message()">click</button>
    </div>
</template>
<script setup lang="ts">

    let dataHere: any
    async function message(){
        await $fetch('http://127.0.0.1:8000/message/message/',{
            method: 'POST',
            body: {
                content: "First post from web"
            }
        })
    }
    async function get_message(){
        dataHere = await $fetch('http://127.0.0.1:8000/message/get_all/',{
            method: 'get',
        })
        console.log(dataHere)
    }
    message()
</script>
<style>
    
</style>