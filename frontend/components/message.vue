<template>
    <div class="w-full px-5 py-2 flex items-center justify-end">
        <div class="flex flex-row items-center justify-center bg-[#b8a6a6] max-w-[870px] min-w-[200px] gap-2 p-2 rounded-lg">
            <p class="flex-1 text-right break-words break-all p-2" v-html="props.msg">
            </p>
            <p class="w-5">
                {{ props.author }}
            </p>
        </div>
    </div>
</template>
<script setup lang="ts">
const props = defineProps(['author', 'msg', 'curAuthor'])
</script>
<style>
    
</style>