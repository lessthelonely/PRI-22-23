<template>
    <nav class="navbar navbar-light navbar-expand-md" id="mainNav"
        style="color: rgb(0,0,0);background: rgb(255,255,255);">
        <div class="container"><a class="navbar-brand" href="#" style="width: 100px;">
                <img src="../assets/images/logo_black.png" style="width: 100%;"></a><button data-bs-toggle="collapse"
                class="navbar-toggler navbar-toggler-right" data-bs-target="#navbarResponsive" type="button"
                aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation" value="Menu"><i
                    class="fa fa-bars"></i></button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item nav-link" style="color: #000000;">
                        <a class="nav-link " href="/" style="color: rgb(0,0,0);">Home</a>
                    </li>
                    <li class="nav-item nav-link" style="color: #000000;">
                        <a class="nav-link " href="/search" style="color: rgb(0,0,0);">Search</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script lang="js">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'WhiteNavbar',
    setup() {
        return {};
    },
});
</script>