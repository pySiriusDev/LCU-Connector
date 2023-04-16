export default defineAppConfig({
  docus: {
    title: "LCU Connector",
    description: "Easy-to-use wrapper for the League Client API.",
    socials: {
      github: "pySiriusDev",
      twitter: "_siriusbeck",
      instagram: "biellviana",
    },
    header: {
      logo: true,
      title: "LCU Connector",
      showLinkIcon: true,
      exclude: [],
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
        icon: "",
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
});
