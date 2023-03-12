<script lang="ts">
  import { receivedStore } from '$lib/store';
  import { onMount } from 'svelte';
  onMount(async () => {
  });
</script>

<svelte:head>
  <title>Home</title>
  <meta name="description" content="Warp Implementation" />
</svelte:head>

<section>
  <h2>wassup</h2>
  <ul>
    {#each $receivedStore as e}
    <li>{e}</li>
    {/each}
  </ul>
</section>

<style lang="scss">
  h2 {
    margin: 0;
  }
</style>
