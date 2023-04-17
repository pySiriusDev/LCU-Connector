export default defineAppConfig({
  docus: {
    title: "LCU Connector",
    description: "Easy-to-use wrapper for the League Client API.",
    url: "https://lcu-connector.vercel.app/",
    image: "https://raw.githubusercontent.com/pySiriusDev/lcu-connector/main/docs/public/cover.png",
    socials: {
      github: "pySiriusDev",
      twitter: "_siriusbeck",
      instagram: "biellviana",
    },
    header: {
      logo: true,
      title: "LCU Connector",
      showLinkIcon: true,
      fluid: false,
    },
    main: {
      fluid: false,
      padded: true,
    },
    aside: {
      level: 0,
      exclude: [],
    },
    footer: {
      credits: {
        icon: "IconLcuC",
        text: "Developed by: Sirius Dev",
        href: "https://github.com/pySiriusDev",
      },
      fluid: false,
    },
    github: {
      edit: false,
    },
  },
  prose: {
    copyButton: {
      iconCopy: "fluent:copy-24-regular",
      iconCopied: "fluent:copy-24-filled",
    },
  },
  colorMode: {
    preference: 'dark'
  },
});
