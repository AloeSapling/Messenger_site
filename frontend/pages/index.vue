<template>
    <div class="max-h-[100vh] flex flex-col h-[100vh]">
        <div class="h-[70px] flex flex-row justify-center items-center gap-3">
            <p>author:</p>
            <input type="text" v-model="author" class="border-black border-[1px] rounded-lg p-1">
        </div>
        <div class="flex-1 overflow-y-auto bg-[#02030d]">
            <Message v-for="message in messages.contents" :author="message.author" :msg="message.message" :curAuthor="author"></Message>
        </div>
        <div class="gap-5 flex flex-row justify-end py-4 px-16 border-t-[3px] border-t-[#9898a5] bg-[#02030d] w-full">
            <div class="border-[#9898a5] border-[1px] rounded-lg px-3 py-1 bg-transparent text-white flex-1 break-words max-h-[150px] overflow-y-auto break-all" contenteditable="true" @keyup="(e)=>{content.value=e.target.innerHTML;console.log(e.target.innerHTML,content.value)}"></div>
            <button @click="message(content.value)" class="text-white">
                <Icon icon="ri:send-plane-fill" width="30"/>
            </button>
        </div>
    </div>
</template>
<script setup lang="ts">
    import Message from '~/components/message.vue';
    import { Icon } from '@iconify/vue/dist/iconify.js';
    const chatSocket = new WebSocket('ws://127.0.0.1:8000/ws/chat/1/');
    let dataHere: any
    let author = 0
    const content = reactive({
        value: ''
    })
    const messages: any = reactive({
            contents: []
        }
    )   
    async function message(msg: string){
        // await $fetch('http://127.0.0.1:8000/message/message/',{
        //     method: 'POST',
        //     body: {
        //         content: "First post from web"
        //     }
        // })
        console.log(msg)
        const message = {
                'message': msg,
                'author': author
            };
        chatSocket.send(JSON.stringify(message));
    }
    async function get_message(){
        dataHere = await $fetch('http://127.0.0.1:8000/message/get_all/',{
            method: 'get',
        })
        console.log(dataHere)
    }
    // message()
    chatSocket.onopen = function() {
        console.log('WebSocket connection established.');
    };
    chatSocket.onmessage = function(event) {
        const message = JSON.parse(event.data);
        console.log('Received message:', message);
        messages.contents.push(message)
    };
</script>
<style>
    
</style>