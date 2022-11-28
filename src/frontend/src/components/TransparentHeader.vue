<template>
    <nav class="navbar navbar-light navbar-expand-md fixed-top" id="mainNav">
        <div class="container">
            <a class="navbar-brand" href="#" style="width: 100px;">
                <img src="../assets/logo.png" style="width: 100%;">
            </a>
            <button data-bs-toggle="collapse" class="navbar-toggler navbar-toggler-right" data-bs-target="#navbarResponsive" type="button" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation" value="Menu"><i class="fa fa-bars"></i></button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item nav-link"><a class="nav-link active" href="#about">About</a></li>
                    <li class="nav-item nav-link"><a class="nav-link" href="#contact">contact</a></li>
                    <li class="nav-item nav-link"><a class="nav-link active" href="#about">search</a></li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script lang="js">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'Navbar',
    setup() {
        return {};
    },
});
</script>