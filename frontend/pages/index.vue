<template>
    <div>
        <p>Hello world</p>
        <button @click="websocketTest()">click</button>
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
    // message()
    async function websocketTest(){
        const chatSocket = new WebSocket('ws://127.0.0.1:8000/ws/chat/');

        chatSocket.onopen = function() {
            console.log('WebSocket connection established.');
            const message = {
                'message': 'Hello, world!'
            };
            chatSocket.send(JSON.stringify(message));
        };
        chatSocket.onmessage = function(event) {
            const message = JSON.parse(event.data);
            console.log('Received message:', message);
        };
    }
</script>
<style>
    
</style>