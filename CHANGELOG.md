<!-- insertion marker -->
<a name="0.1.0"></a>

## [0.1.0](https://github.com///compare/e5bd4d069fb126a5b9f8597ae4235f19f1c137e9...0.1.0) (2025-10-27)

### Features

- add default value for pad_token in SeqClassificationTorchDataset constructor ([f97cb47](https://github.com///commit/f97cb47226cbc4c186583c98fa8d768f47a80870))
- rename dataset class for sequence classification and update preprocessing to return max length ([bcecb96](https://github.com///commit/bcecb968a174dfc8995902aa8cf30ded937e90dd))
- rename and enhance dataset classes for sequential prediction and classification ([3bd37cc](https://github.com///commit/3bd37cc8576fabd870239c4ba0ae4b482e656c35))
- update word processing to retain only lowercase English words ([f0ce448](https://github.com///commit/f0ce448570da2ad59b0fde3ae234990832036c48))
- implement data preprocessing and dataset preparation functions with tokenization and vocabulary mapping ([41d3ad1](https://github.com///commit/41d3ad138e070f656436c832a91560fb088dbd02))
- add function to load text data from directory with progress tracking ([1b1c43e](https://github.com///commit/1b1c43e032a243a754a1859c6632bc6bda087286))
- add initial dictionary.json for NLP model vocabulary ([9964289](https://github.com///commit/9964289e95c4ad29ccdb05f1aea110cc119bb37c))
- add spacy-pkuseg package for improved tokenization capabilities ([4cfb11c](https://github.com///commit/4cfb11cf50687840ef535ce11070733b8cabae46))
- add spacy-pkuseg dependency for enhanced tokenization support ([7fd90cd](https://github.com///commit/7fd90cd5f3f412beccba3abbf8e48123681b8946))
- implement SpaCy and Stanza tokenizers for English and Chinese text processing ([73314f7](https://github.com///commit/73314f7adb17e43edcdc2917f24d226080fda5fc))
- integrate Spacy and Stanza tokenizers for English and Chinese text processing ([74ddc00](https://github.com///commit/74ddc008919780237dc5210e0a54c8180bf5136b))
- add file paths for Spacy and Stanza models, and training/testing datasets ([b1d7407](https://github.com///commit/b1d7407ce82a19074613072caac4b6f565cb9767))
- add CHANGELOG.md for version 0.1.0 with features and bug fixes ([0083342](https://github.com///commit/0083342a09441f8cc0b3afadff592fbd1c73dbbb))
- add an uv file ([f3ba4dd](https://github.com///commit/f3ba4dd8196ef47e3ce4b9743f8a3c2465a8eff0))
- implement RegressionTrainer class for model training and validation ([22e3c8a](https://github.com///commit/22e3c8a123612761379ba4614c107e589cbff1f5))
- add THULAC text segmentation functions for Chinese NLP processing ([cc0159b](https://github.com///commit/cc0159bdf645a01ef5acf758099ddd09df55e3d5))
- implement data processing functions including loading, preprocessing, and PCA feature importance ([7e84916](https://github.com///commit/7e84916464a453fbd9e7ace6097423eaa1d898b9))
- implement SpaCy NLP processor for English text tokenization and lemmatization ([6c1b2cb](https://github.com///commit/6c1b2cbc7dcfa5cff98005e8b622433300d0300d))
- add additional dependencies for Chinese NLP support in requirements.txt ([75b543b](https://github.com///commit/75b543bd7c02c794e2318415c08c66f161d154e2))
- update Chinese README to reflect focus on sentiment analysis using IMDB dataset ([6782e3e](https://github.com///commit/6782e3e3676fb76445b7029e11ab4f20ea0fda6a))
- update README to reflect focus on sentiment analysis of movie reviews using IMDB dataset ([9a5b214](https://github.com///commit/9a5b21467c2d3a469dab5e62145a26c6f7873c47))
- add dependencies for Chinese text processing and NLP support ([de2c6d3](https://github.com///commit/de2c6d34b8d7a520efcf8af2a1dd487f41fdb2eb))
- implement TorchRandomSeed, TorchDataLoader, and custom Dataset classes for PyTorch integration ([a3a1ca6](https://github.com///commit/a3a1ca6e842f841f958eabcbb33517a501f49c1b))
- implement Outputter class for controlled message printing ([2730e53](https://github.com///commit/2730e531a3c6374ab649ad3d1c9704b3b179ae5b))
- add functions for processing and analyzing Chinese and English text, including character extraction and word frequency analysis ([60fd5a6](https://github.com///commit/60fd5a636c0894aae040dc3c524dc169ed1375a6))
- integrate snlp_analysis for Chinese text processing in main function ([c5eb5be](https://github.com///commit/c5eb5be8767154e04c6672d64726e4d3e648e35a))
- add jieba text processing functions with performance tracking ([49c93a5](https://github.com///commit/49c93a5580501df12a9bc7537a0fcfadb11ad25b))
- add text highlighting functions and formatting utilities for improved output presentation ([5621019](https://github.com///commit/5621019a6f732bfa695ae0af25bd596515f688d3))
- add Timer, Beautifier, and RandomSeed context managers for enhanced code performance tracking and readability ([7531dba](https://github.com///commit/7531dbabb7693a2083bfc8d4fa5246c15cfedab8))
- add timer and beautifier decorators for function performance tracking ([d12ec08](https://github.com///commit/d12ec0892f3620ab787b167b960b7011d52646f5))
- implement log_mse_loss function for regression tasks ([e11c251](https://github.com///commit/e11c251f2443fafd1bc42fa714362a29d2c1e2f3))
- add configuration classes for file paths, data preprocessing, model parameters, and hyperparameters ([5e7d385](https://github.com///commit/5e7d385a42f472c713f53123d915e472f6bd2b62))

### Bug Fixes

- ensure main function is called and add newline at end of file ([097dcd8](https://github.com///commit/097dcd80ba540830cde95dd2cbaf318766fb893f))
- add missing newline at end of file and ensure main function is called ([bea5df5](https://github.com///commit/bea5df5c434698f62a1d749a4c202968dc4f3394))

### Docs

- add data description and details to Chinese README ([40132d7](https://github.com///commit/40132d7424b7c9b44a518998df349773f30a32e0))
- add dataset description and details to README ([6460915](https://github.com///commit/64609153010ed775f4b772827b499e2b9db5f9e4))
- update CHANGELOG.md for version 0.1.0 with recent dependency additions ([8209c34](https://github.com///commit/8209c3491b93b05f00c7db563af6386005d3c0cb))
- update CHANGELOG.md for version 0.1.0 with recent documentation changes ([5fcc87a](https://github.com///commit/5fcc87af3e89498f870ea2748cf1fc1f25f6edd5))
- fix formatting in README.md for improved readability ([3ab6a50](https://github.com///commit/3ab6a50363433783e5515468c09ba0306dd12250))
- update CHANGELOG.md for version 0.1.0 with new features and documentation updates ([e8aff29](https://github.com///commit/e8aff29224f70fb0de239e0189ba9c3ea3214733))
- add usage instructions for NLP models in README.zh-CN.md ([e945193](https://github.com///commit/e94519336c119a16bd8057e634b9d39bb54d1937))
- update README.md with instructions for downloading NLP models for SpaCy and Stanza ([e7b73d2](https://github.com///commit/e7b73d2af1f93ecc78fa95c61f11633f4ac99f1b))
- delete a package ([94cfda2](https://github.com///commit/94cfda215447c877f081147d1123211bf66d088b))
- update README.md for improved project description and clarity ([f89c612](https://github.com///commit/f89c6127362f100988333403fee281182a982163))

### Code Refactoring

- update data handling and preprocessing functions for improved flexibility and clarity ([d04eadf](https://github.com///commit/d04eadf3c25c28dd8033e692bac6cac93a6ce057))
- remove main function and entry point from predictor.py ([3a58839](https://github.com///commit/3a58839da2001de341b0d06400e0e763df1d2446))
- remove main function and entry point from models.py ([ad66727](https://github.com///commit/ad667275da8c50f6e873baaed1fea828e169c6ec))

### Dependencies

- add spacy-pkuseg requirement for improved NLP model support ([091848c](https://github.com///commit/091848cf1ee26c499ec2928bc08a02b175306f31))

