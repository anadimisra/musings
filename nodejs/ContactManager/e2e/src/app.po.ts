import { browser, by, element } from 'protractor';

export class AppPage {
  navigateTo() {
    return browser.get(browser.baseUrl) as Promise<any>;
  }

  getTitle() {
    return element(by.css('app-root h1'));
  }

  getContactListText() {
    return element(by.css('app-root h1')).getText() as Promise<string>;
  }  
}
