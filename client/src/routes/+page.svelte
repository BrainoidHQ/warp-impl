<script lang="ts">
  import { receivedStore } from '$lib/store';
  import { Warp } from '$lib/warp/warp';
  import { onMount } from 'svelte';
  onMount(async () => {
    try {
      const warp = new Warp();
      await warp.init();
    } catch (e) {
      console.log('something went wrong');
      console.error(e);
    }
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
