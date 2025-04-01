<template>
  <div class="about">
    <div class="about-page">
      <h1>About Me</h1>
    </div>
    <div class="about-page">
      <h3>Hey I'm <span class="green">Muhammad Khalish Madani</span> web developer that specialize in ERP Software</h3>
      <p style="margin-bottom: -1px;">
        <font-awesome-icon :icon="['fab', 'github']" /> my github:
        <a href="https://github.com/KhalishMadani/" target="_blank"> github/khalishmadani</a>
      </p>

      <p>
        <font-awesome-icon :icon="['fab', 'linkedin']" /> my LinkedIn:
        <a href="https://www.linkedin.com/in/madanikhalish/" target="_blank">linkedin/khalishmadani</a>
      </p>
    </div>
  </div>
</template>

<style>
.about {
  display: flex;
  flex-direction: column;
  gap: 1rem
}

@media (min-width: 1024px) {
  .about {
    display: flex;
    align-items: center;
  }
}
</style>
