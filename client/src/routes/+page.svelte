<script lang="ts">
  import { receivedStore } from '$lib/store';
  import { WT } from '$lib/wt';
  import { onMount } from 'svelte';
  let received: string[] = [];
  receivedStore.subscribe((val) => {
    received = val;
  })
  onMount(async () => {
    const wt = new WT('https://0.0.0.0:4433/counter');
    await wt.setup();
    wt.writeDatagram('Hello');
    wt.readDatagram();
  });
</script>

<svelte:head>
  <title>Home</title>
  <meta name="description" content="Warp Implementation" />
</svelte:head>

<section>
  <h2>wassup</h2>
  <ul>
    {#each received as e}
    <li>{e}</li>
    {/each}
  </ul>
</section>

<style lang="scss">
  h2 {
    margin: 0;
  }
</style>
