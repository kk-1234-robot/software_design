<template>
  <div>
    <a-steps
        v-model:current="current"
        direction="vertical"
        size="default"
        :items="[
        {
          title: 'Step 1',
          description: 'This is description 1 This is description 1 This is description 1 This is description 1 This is description 1 This is description 1 This is description 1' +
           ' This is description 1 This is description 1 This is description 1 This is description 1 This is description 1 This is description 1 This is description 1 This is description 1 This is description 1' +
            ' This is description 1 This is description 1 This is description 1 This is description 1 This is description 1 This is description 1',
        },
        {
          title: 'Step 2',
          description: 'This is description 2',
        },
        {
          title: 'Step 3',
          description: 'This is description 3',
        },
      ]"
    ></a-steps>
  </div>
</template>
<script lang="ts" setup>
import {ref} from 'vue';

const current = ref<number>(0);

</script>

<style scoped>

</style>