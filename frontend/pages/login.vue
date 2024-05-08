<template>
    <div>
        <label for="username">Username:</label>
        <input name="username" type="text" v-model="username"/>
    </div>
    <div><label for="password">Password:</label><input type="password" name="password" v-model="password"></div>
    <button @click="submit()">submit</button>
    <button @click="logout()">logout</button>
</template>
<script setup lang="ts">
import {ref, computed} from 'vue'
const username = ref('')
const password = ref('')
async function submit(){
    await $fetch('http://127.0.0.1:8000/user/login/', {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body:JSON.stringify({
            'username': username.value,
            'password': password.value,
        })
    }).then(function(response){
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
</script>
<style lang="">
    
</style>