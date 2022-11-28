<template>
    <TransparentHeader />

    <body id="page-top" data-bs-spy="scroll" data-bs-target="#mainNav" data-bs-offset="77"
        style="display: block; width: 100%;">
        <header
            style="background-image:url('https://media.discordapp.net/attachments/1042104897866301470/1046865776814071808/background.png?width=1178&height=662');">
            <div class="intro-body" style="background: center / auto no-repeat;" id="picture-1">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-8 mx-auto">
                            <h1 class="brand-heading" style="width: 100%;">
                                <img src="../assets/logo.png" style="width: 100%;">
                            </h1>
                            <p class="intro-text" style="font-family: Cabin, sans-serif;">We're not like other girls, we
                                <em>like books</em>.</p><a class="btn btn-link btn-circle" role="button"
                                href="#about"><i class="fa fa-angle-double-down animated"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <section class="text-center content-section" id="about">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 mx-auto" style="font-family: Cabin, sans-serif;">
                        <h2>ABOUT</h2>
                        <p style="font-family: Arial;"><em>Reading is hard.</em> No, we mean it literally.<br></p>
                        <p style="font-family: Arial;">This is why a <em>very </em>competent team has created
                            NOVELideas, which exists to make reading as easy as possible: one doesn't even have to know
                            <em>what&nbsp;</em>they're looking for, only that they're looking for <em>something</em>!
                        </p>
                        <p style="font-family: Arial;">All you have to do is to want to find a new book, and it can be
                            as specific or as vague as you prefer - but what are you doing reading this still? Go try
                            it!</p>
                    </div>
                </div>
            </div>
        </section>
        <section class="text-center download-section content-section" id="picture-2"></section>
        <section class="text-center content-section" id="contact">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 mx-auto">
                        <h2>Contact us</h2>
                        <p style="font-family: Arial;">We really want you to contact us, so use the following links that
                            definitely work!<br>We wouldn't add buttons just because, yeah... totally!</p>
                        <ul class="list-inline banner-social-buttons">
                            <li class="list-inline-item">&nbsp;<button class="btn btn-primary btn-lg btn-default"
                                    type="button"><i class="far fa-envelope fa-fw"></i><span class="network-name">&nbsp;
                                        E-mail</span></button></li>
                            <li class="list-inline-item">&nbsp;<button class="btn btn-primary btn-lg btn-default"
                                    type="button"><i class="fa fa-twitter fa-fw"></i><span
                                        class="network-name">&nbsp;Twitter</span></button></li>
                            <li class="list-inline-item">&nbsp;<button class="btn btn-primary btn-lg btn-default"
                                    type="button"><i class="fa fa-github fa-fw"></i><span
                                        class="network-name">&nbsp;github</span></button></li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
        <div class="map-clean"></div>
        <footer>
            <div class="container text-center">
                <p style="font-size: 11px;">Copyright ©&nbsp;NOVELIDEAS 2022</p>
            </div>
        </footer>
    </body>
</template>

<script lang="js">
import { defineComponent } from 'vue';
import TransparentHeader from '../components/TransparentHeader.vue';

export default defineComponent({
    name: 'Home',
    components: {
        TransparentHeader
    }
});
</script>