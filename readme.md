## Getting Started

This code uses python to take a csv file and load it into a bigquery table.

### Prerequisites

1. Have python3 installed

2. Make sure to enable the [Identity and Access Management API](https://console.cloud.google.com/flows/enableapi?apiid=iam.googleapis.com&redirect=https://console.cloud.google.com&_ga=2.216173078.1847126783.1686858471-890984077.1685987531) for your GCP Account

3. Create a service account that has the BigQuery Admin Role and then [generate a service account key](https://www.youtube.com/watch?v=dj9fxiuz4WM) and place your service account key json file in the keys folder.

### Installation

1. Create virtual envinonment in repo directory

   ```
   python3 -m venv ./venv
   ```

2. Activate the virtual environment

   ```
   source ./venv/bin/activate
   ```

3. Install Requirements
   ```
   pip install requirements.txt
   ```

<!-- USAGE EXAMPLES -->

## Usage

To use this app, edit the config file with your filenames and your bigquery informaiton. Then run the app.py file and it should creat or append the information from your csv file.

<!-- CONTRIBUTING

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request -->
<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->

## Contact

Ben Q - ben@vineskills.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)
