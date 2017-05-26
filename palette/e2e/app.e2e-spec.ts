import { PalettePage } from './app.po';

describe('palette App', () => {
  let page: PalettePage;

  beforeEach(() => {
    page = new PalettePage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
