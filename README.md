# mac-audio-hackery

---

# Why Can't My Mac Just Listen to Itself? 

![](https://media.licdn.com/dms/image/v2/C4D12AQF1b012ufBTuQ/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1520123016295?e=2147483647&v=beta&t=SO-VAEw8E3EyzYYreR2IVxuVTgr4oQ-B7P9swVOUW1A)

Recording audio on a Mac has never been more straightforward, thanks to the plethora of high-quality built-in and third-party tools available. However, one persistent challenge remains for many users: capturing audio from both the microphone and the system speakers simultaneously. Whether you're a content creator, podcaster, or remote worker, this limitation can hinder your ability to produce comprehensive and professional-grade recordings.

By integrating BlackHole 2ch with Multi-Output and Aggregate Devices, you can overcome macOS's native limitations to capture both microphone and system audio simultaneously. 

---

### Understanding the Problem
 
At its core, the issue stems from how macOS handles audio input and output. By default, macOS restricts audio capture to a single input or output source at a time. This means that when you attempt to record audio, you can choose either the microphone (for input) or the system speakers (for output), but not both simultaneously. This limitation becomes problematic in scenarios where capturing both sources is essential, such as:

Podcasts and Interviews: Where you want to record your voice through a microphone while also capturing audio from a remote guest via system speakers.
Gaming and Streaming: To record gameplay sounds alongside your commentary.
Virtual Meetings and Tutorials: Where you need to showcase system audio (like application sounds) along with your narration.

Without the ability to record both audio streams, achieving high-quality, integrated recordings becomes challenging.

### Why Does This Limitation Exist?
 
The macOS audio architecture is designed with simplicity and resource optimization in mind. By default, it prioritizes a single audio stream to ensure stability and reduce potential conflicts between multiple audio sources. This design choice minimizes the risk of audio lag, feedback loops, and other sound quality issues that can arise from handling multiple audio inputs and outputs simultaneously.

Moreover, the macOS security framework imposes strict permissions on audio recording to protect user privacy. Allowing multiple audio streams to be captured without explicit user consent could lead to potential misuse, such as unauthorized recording of system sounds or other sensitive audio data.

#### **Legal and Information Security Implications**

Recording system audio and microphone input simultaneously introduces privacy and legal considerations, particularly when the recordings involve other people or sensitive content. While macOS’s restrictions partially address these concerns, bypassing them through third-party tools necessitates heightened awareness and responsibility.

1. **Consent Laws**  
   - **Single-Party Consent**: In some jurisdictions, only one party (e.g., yourself) needs to consent to recording a conversation or audio.  
   - **Two-Party Consent**: Other regions require all parties involved in a conversation to provide explicit consent before recording.  
   - **System Audio Implications**: When recording system audio, ensure that any audio output, such as conference calls or streaming content, complies with copyright and consent laws.

   **Recommendation**: Always inform participants if their audio is being recorded and secure explicit consent where required. This is especially critical for public-facing use cases like podcasting, streaming, or live events.

2. **Privacy Risks**  
   - **Sensitive Content**: System audio may inadvertently include sensitive or private information, such as notifications, private calls, or system alerts.  
   - **Data Security**: If the recordings contain proprietary or sensitive data, ensure they are stored securely and only shared with authorized individuals.

   **Best Practices**: Use headphones during recording to limit the scope of captured audio, and verify that only intended audio streams are being recorded.

3. **Organizational Compliance**  
   - **Corporate Policies**: Organizations may have strict policies regarding the recording of system audio, especially in regulated industries like healthcare, finance, or education.  
   - **Infosec Measures**: Ensure recordings comply with organizational data security policies, including encryption and restricted access.

   **Recommendation**: Before recording in a professional setting, consult your organization’s compliance or legal team to understand applicable regulations.

---

# Capturing Both Microphone and System Audio on Mac
  
Recording both microphone input and system audio simultaneously on a Mac can be challenging due to macOS's native limitations. However, by leveraging **BlackHole 2ch**, creating a **Multi-Output Device**, and configuring a **Custom Aggregate Device**, you can effectively bypass these restrictions. This setup is particularly useful when working with audio processing scripts, such as the Python code provided below, which utilizes **PyAudio** to record and transcribe audio using Deepgram's API.  
  
In this blog post, we'll walk you through:  
  
1. **Setting Up BlackHole 2ch and Aggregate Devices on macOS**  
2. **Configuring Your Python Script to Capture Both Audio Streams**  
3. **Running and Testing the Setup**  
  
By the end of this guide, you'll have a comprehensive understanding of how to integrate system audio and microphone input into your Python applications seamlessly.  
  
---  
  
## Understanding the Components  
  
Before diving into the setup, it's crucial to understand the role of each component involved:  
  
- **BlackHole 2ch**: An open-source virtual audio driver for macOS that allows applications to pass audio to other applications with zero additional latency.  
    
- **Multi-Output Device**: A configuration in macOS that lets you send audio to multiple outputs simultaneously, such as your speakers and BlackHole.  
  
- **Aggregate Device**: A combination of multiple audio devices into a single virtual device, enabling simultaneous input from sources like your microphone and system audio.  
  
- **PyAudio**: A Python library that provides bindings for PortAudio, allowing you to record and play audio in Python scripts.  
  
- **Deepgram API**: A speech recognition service that can transcribe audio data, including features like speaker diarization.  
  
---  
  
## Step 1: Install BlackHole 2ch  
  
**BlackHole 2ch** acts as a bridge between your system audio and recording applications. Here's how to install and verify it:  
  
### Installation Steps:  
  
1. **Download BlackHole 2ch:**  
   - Visit the [BlackHole GitHub repository](https://github.com/ExistentialAudio/BlackHole) or the official [BlackHole website](https://existential.audio/blackhole/) to download the installer.  
  
2. **Run the Installer:**  
   - Open the downloaded package and follow the on-screen instructions to install BlackHole 2ch on your Mac. You might need to grant necessary permissions during installation.  
  
3. **Verify Installation:**  
   - Open **Audio MIDI Setup** (found in **Applications > Utilities**).  
   - Ensure that **BlackHole 2ch** appears in the list of audio devices under both **Input** and **Output** sections.  
  
---  
  
## Step 2: Create a Multi-Output Device  
  
A **Multi-Output Device** allows your Mac to send audio to both your speakers (or headphones) and BlackHole simultaneously. This setup ensures you can hear the system audio while it's being routed for recording.  
  
### Setup Steps:  
  
1. **Open Audio MIDI Setup:**  
   - Navigate to **Applications > Utilities > Audio MIDI Setup**.  
  
2. **Create Multi-Output Device:**  
   - Click the **"+"** button in the bottom-left corner and select **"Create Multi-Output Device"**.  
  
3. **Configure Multi-Output Device:**  
   - In the newly created Multi-Output Device, check the boxes for:  
     - **BlackHole 2ch**  
     - Your primary audio output device (e.g., **MacBook Pro Speakers**, **Headphones**, etc.)  
  
4. **Set Default Output:**  
   - Right-click (or Control-click) the Multi-Output Device and select **"Use This Device For Sound Output"**.  
  
5. **Enable Drift Correction:**  
   - Ensure **Drift Correction** is enabled for **BlackHole 2ch** to maintain audio synchronization.  
  
---  
  
## Step 3: Set Up an Aggregate Device for Input  
  
The **Aggregate Device** combines your microphone and the system audio (routed through BlackHole) into a single input source for your recording application.  
  
### Setup Steps:  
  
1. **Open Audio MIDI Setup:**  
   - If not already open from the previous step, navigate to **Applications > Utilities > Audio MIDI Setup**.  
  
2. **Create Aggregate Device:**  
   - Click the **"+"** button and select **"Create Aggregate Device"**.  
  
3. **Configure Aggregate Device:**  
   - In the Aggregate Device, check the boxes for:  
     - **Built-in Microphone** (or your preferred external microphone)  
     - **BlackHole 2ch**  
  
4. **Name the Aggregate Device:**  
   - Double-click the name (e.g., **Aggregate Device**) and rename it to something descriptive like **"Microphone + System Audio"**.  
  
5. **Set Input Source:**  
   - Open **System Preferences > Sound > Input** and select your newly created Aggregate Device (**"Microphone + System Audio"**) as the input source.  
  
---  
  
## Conclusion

While technological solutions like BlackHole and Aggregate Devices empower users to overcome macOS’s limitations, it’s essential to balance these capabilities with ethical and legal responsibility. Recording audio without consent or capturing unintended system sounds can result in serious legal and reputational consequences.

By staying informed about local laws, securing proper permissions, and implementing privacy-conscious practices, you can ensure that your recordings are both effective and responsible.
 
By setting up BlackHole 2ch alongside customized Multi-Output and Aggregate Devices, we've effectively circumvented macOS's inherent limitations regarding simultaneous audio input and output capture. This configuration allows for seamless recording of both your microphone and system audio, enabling more comprehensive audio processing and recording capabilities in applications like Python scripts using PyAudio.

Whether you're conducting interviews, recording podcasts, streaming, or developing audio-processing applications, this setup provides a versatile solution that integrates both audio streams into your workflow. By leveraging open-source tools and macOS's built-in audio utilities, you can achieve professional-level audio recording without the need for expensive third-party software.

---

### Appendix: Additional Resources and Legal Considerations

---

#### **Appendix: Troubleshooting and Resources**

1. **Troubleshooting Tips**  
   - **Audio Sync Issues**: If audio from the system and microphone becomes unsynchronized, double-check that Drift Correction is enabled in your Multi-Output Device.  
   - **No Sound in Recording**: Ensure your recording software is configured to use the Aggregate Device as the input source.  
   - **BlackHole Not Appearing**: Restart your Mac and verify BlackHole is installed correctly in the Audio MIDI Setup tool.  

2. **Recommended Tools**  
   - **Audio Hijack (Paid Alternative)**: Rogue Amoeba’s Audio Hijack offers advanced audio routing features for users seeking a polished, professional-grade solution.  
   - **GarageBand**: For users already familiar with Apple’s ecosystem, GarageBand supports audio input selection, which can leverage Aggregate Devices for multi-source recording.

3. **Further Reading**  
   - [BlackHole GitHub Documentation](https://github.com/ExistentialAudio/BlackHole)  
   - [Apple's Audio MIDI Setup User Guide](https://support.apple.com/guide/audio-midi-setup)  
   - [Deepgram’s Python SDK Documentation](https://github.com/deepgram/py-sdk)
