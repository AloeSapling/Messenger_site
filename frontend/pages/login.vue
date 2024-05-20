<template>
    <div>
        <label for="username">Username:</label>
        <input name="username" type="text" v-model="username"/>
    </div>
    <div><label for="password">Password:</label><input type="password" name="password" v-model="password"></div>
    <button @click="submit()">submit</button>
    <button @click="logout()">logout</button>
    <input v-model="room"/>
        <button @click="join()">join</button>
        <button @click="get()">get</button>
</template>
<script setup lang="ts">
import {ref, computed} from 'vue'
const username = ref('')
const password = ref('')
let sess: string;
async function submit(){
    await fetch('http://127.0.0.1:8000/user/login/', {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body:JSON.stringify({
            'username': username.value,
            'password': password.value,
        })
    }).then(function(response: any){
        console.log(response)
    })
    // console.log(await $fetch('http://127.0.0.1:8000/message/get_all/',{
    //     method: 'GET'
    // }))
}
async function logout(){
    await $fetch('http://127.0.0.1:8000/user/logout/', {
        method: 'PUT'
    })
}
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
    async function get(){await $fetch('http://127.0.0.1:8000/message/get_all/',{
        method: 'GET',
        credentials:'include',
        headers: {
            'cookie': `sessionid=${sess}; Expires=Thu, 30 May 2024 09:03:41 GMT; Max-Age=1209600; Domain=127.0.0.1; Path=/; Secure`
        }
    })}
</script>
<style lang="">
    
</style>