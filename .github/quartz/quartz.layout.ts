import { PageLayout, SharedLayout } from "./quartz/cfg";
import * as Component from "./quartz/components";

export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      "Главная страница": "https://vlsu-hub.org",
      Telegram: "https://t.me/the_nataraja",
      GitHub: "https://github.com/vlsu-hub/obsidian-base",
    },
  }),
};

export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs(),
    Component.ArticleTitle(),
    Component.ContentMeta({ showReadingTime: false }),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.ReaderMode(),
    Component.Explorer({
      title: "Навигация",
      useSavedState: true,
      folderClickBehavior: "collapse",
      folderDefaultState: "collapsed",
    }),
  ],
  right: [
    Component.Graph(),
    Component.TableOfContents({
      layout: "modern",
    }),
    Component.Backlinks(),
  ],
};

export const defaultListPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs(),
    Component.ArticleTitle(),
    Component.ContentMeta({ showReadingTime: false }),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.ReaderMode(),
    Component.Explorer({
      title: "Навигация",
      useSavedState: true,
      folderClickBehavior: "collapse",
      folderDefaultState: "collapsed",
    }),
  ],
  right: [],
};
