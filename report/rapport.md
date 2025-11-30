# Accelerometer-based measurement to quantify muscle fatigue

**Authors :** Mahoua KONE, Lucie BONNOT, Loubna EL FARESSI, Bomane PEHE 
**Date :** November 10, 2025  
**Supervisor :** Denis MOTTET

---

## 1. Introduction

   Muscular fatigue is characterized by a progressive decline in a muscle’s ability to generate force, manifesting as alterations in movement execution, reduced range of motion, or decreased regularity. Although physiological tools such as electromyography, heart rate monitoring, or blood lactate assessment can be used to quantify fatigue, these methods are often costly, invasive, or difficult to implement in real-world conditions.

Inertial sensors, particularly accelerometers, offer a simple, portable, and non-invasive alternative for analyzing movement dynamics. By measuring acceleration along three axes, they provide a quantitative estimation of movement intensity, notably through the acceleration norm.

In this project, we examined the evolution of acceleration signals during a jump-rope exercise. The objective was to determine whether sensor placement influences the ability to detect muscular fatigue throughout the task. Two locations were tested within the same session:
 * the right wrist, primarily involved in rope rotation,
 * the right ankle, directly associated with take-off and landing phases.

Our hypothesis is that the dynamics of the acceleration signal vary with sensor location, as these body segments experience different biomechanical constraints. More specifically, we assume that the ankle-mounted sensor may better capture indicators of muscular fatigue, as it measures variations related to propulsion, stability, and impact forces during jumps, whereas the wrist mainly reflects rope rotation, which is less affected by lower-limb fatigue.

To test this hypothesis, the acceleration signal was analyzed over the full duration of the exercise and segmented into normalized time intervals, allowing the evolution of movement intensity from the beginning to the end of the session to be observed. The resulting acceleration distributions were then compared between the two sensor positions in order to identify which location provides the most relevant information for detecting signs of muscular fatigue during jump-rope exercise.

## 2. Materials and Methods

### 2.1. Materials

The study was conducted using an Axivity AX3 tri-axial accelerometer (Axivity Ltd., United Kingdom), an inertial device widely employed in movement science for the quantification of physical activity. The AX3 is a standalone data logger incorporating a tri-axial MEMS sensor, an internal clock, and flash memory for continuous data recording. It connects to a computer via USB for configuration, data transfer, and battery charging.

The sensor was configured with a sampling frequency of 100 Hz and a measurement range of ±8 g, parameters suitable for capturing rapid movements such as jump-rope exercise. It was securely attached to the investigated body region (wrist or ankle) to minimize artifacts caused by extraneous motion. After completion of the exercise, the recordings were exported in CSV format using the OmGui software (Axivity Ltd.).


### 2.2. Experimental Protocol

### 2.2.1 General Description

The study was conducted with a voluntary female participant, a student, who presented no known locomotor disorders or functional limitations.
The participant performed a jump-rope exercise at a self-selected intensity for a duration sufficient to induce progressive muscular fatigue.

Two triaxial accelerometers were used simultaneously during the exercise: one attached to the right wrist, primarily reflecting rope rotation, and the other attached to the right ankle, directly associated with take-off and landing phases of the jumps.

This protocol enables the recording, for the same movement and at the same instant, of two acceleration signals corresponding to two distinct body segments. The aim is to compare the temporal dynamics of these signals in order to determine which sensor location is most relevant for detecting potential indicators of muscular fatigue during jump-rope exercise.

| Sensor                         | Body location | Exercise   | Recording mode |
|-------------------------------|---------------|------------|----------------|
| Axivity AX3, 100 Hz sampling rate | Right wrist   | Jump rope  | Simultaneous   |
| Axivity AX3, 100 Hz sampling rate | Right ankle   | Jump rope  | Simultaneous   |

**Table 1 : Experimental Conditions**

### 2.2.2 Programming and configuring the sensor:

Before each measurement, the Axivity AX3 sensor was configured using the OmGui software (Axivity Ltd.). This software allows sensors to be set up, initialized, and synchronized prior to data recording.

Here is the website link:[Texte du lien](https://axivity.com/userguides/omgui/)

The configuration steps were as follows:
1. Sensor connection: The sensor is connected to the computer via a micro-USB type B cable. It automatically appears in the Device Browser Pane of the OmGui software.
2. Clearing previous data: The Clear button is used to delete any prior recordings stored in the sensor’s internal memory, ensuring a blank data file for each test.
3. Acquisition parameter settings:
    * Sampling frequency: 100 Hz
    * Measurement range: ±8 g
    * Start mode: Start at programmed time
    * Synchronization: the sensor’s internal clock is automatically adjusted to the computer’s time at validation.
4. Start time programming: The sensor was programmed to automatically begin recording at the predefined time set in the software (interval start time). Once disconnected from the computer, the device remained in standby until the scheduled time was reached, at which point recording started autonomously.

### 2.2.3 Data Collection and Transfer:

The participant performed three series of jump-rope exercise: the first lasted 4 minutes and the following two lasted 5 minutes each.

A 5-minute rest period was provided between series. This pause allowed the experimenter to: download the recorded data, reprogram the sensors for the next trial, and provide brief muscular recovery before resuming the exercise.

At the end of each series, the accelerometers were reconnected to the computer to retrieve the data. The recording was stopped using the Stop command, then the Download function was used to transfer the file in .CWA format to the OmGui Working Folder.

The recordings were initially saved in the proprietary .CWA binary format, which is not directly compatible with standard data-analysis tools. To process the data in Python, the files were converted into .CSV format using the Export raw data to CSV function in OmGui.

The following export parameters were selected:
- Accelerometer units: Gravity (g), i.e. acceleration expressed in multiples of g (1 g = 9.81 m·s⁻²)
- Timestamp estimation: Formatted (Y–M–D h:m:s.f), providing precise and readable timestamps
- Sub-sampling: disabled, ensuring that the entire raw signal was preserved

The resulting CSV files contained four columns: timestamp, X-axis acceleration, Y-axis acceleration, and Z-axis acceleration. These files were subsequently used for numerical processing, statistical computation (RMS, ENMO, etc.), and graphical visualization in Python.

## 3. Measurement Methodology for Acceleration Signals

To assess whether sensor placement (ankle vs. wrist) influences sensitivity to muscle fatigue, we processed the raw triaxial acceleration signals from both locations using the same metric and workflow. The analysis relied on the Euclidean Norm Minus One (ENMO), a widely used index of movement intensity derived from triaxial accelerometer data. ENMO reflects the magnitude of acceleration above 1 g (gravitational acceleration) and therefore quantifies active movement only.

 ### 3.1. Pre-processing of acceleration signals

To ensure consistent processing across both sensor locations, the raw triaxial acceleration data were first combined into a single magnitude representing overall movement intensity. 

$$
\text{Norm} = \sqrt{a_x^2 + a_y^2 + a_z^2}
$$

Movement-related acceleration was then extracted using the Euclidean Norm Minus One (ENMO) metric, which removes the constant gravitational component so that only dynamic motion remains.

$$
\text{ENMO} = \max(\text{Norm} - 1, 0)
$$

Time was normalized for each trial by subtracting the initial timestamp, allowing direct temporal comparison between wrist and ankle recordings.

### 3.2. Sliding-window ENMO integration (10, 20, 30 s)
To examine how movement intensity evolved throughout the exercise, ENMO was integrated over sliding time windows of 10, 20, and 30 seconds. 

$$
\text{ENMO}_{\text{integrated}}(t) = \sum_i \text{ENMO}_i \cdot \Delta t_i
$$

For each window duration, ENMO values were multiplied by the sampling interval and summed over the window, producing a continuous curve that reflects short-term variations in movement dynamics.

$$
\text{ENMO}_{L_s}(t) = \sum_{i = t-L_s}^{t} \text{ENMO}_i \cdot \Delta t_i
$$

These sliding-window curves reveal gradual changes in jump amplitude, impact forces, and coordination that may indicate the onset of muscular fatigue.

### 3.3. Fixed-window ENMO integration (10, 20, 30 s)

To compare corresponding moments of the exercise between the two sensor locations, the ENMO signal was also segmented into non-overlapping fixed windows of 10, 20, and 30 seconds. For each window, total movement intensity was computed, providing one representative value per segment.

$$
\text{ENMO}_{L_s}^{(k)} = \sum_{i \in W_k} \text{ENMO}_i \cdot \Delta t_i,
\qquad
W_k = [kL,\,(k+1)L]
$$

These fixed-window values form a discrete intensity profile, enabling direct ankle–wrist comparison at identical time intervals during the session.

### 3.4. ENMO Boxplot Analysis: Global Distribution Across Sensor Locations

To simplify the overall analysis of the signal, we also represented the data using boxplots. The objective was to obtain a direct and 
intuitive visualization of the ENMO distribution for each series by comparing the ankle and the wrist on the same graph.
Thus, we produced three separate figures: one for Series 1, one for Series 2, and one for Series 3. Each graph includes two boxplots, one for the ankle sensor and the other for the wrist sensor, which allows for a quick comparison of intensity levels, signal dispersion, and extreme values between the two locations, and highlights the global differences between the sensors across the different series.

## 4- Results
### 4-1- Time-series analysis of instantaneous ENMO

The data analysis leads to the results presented below. Figure 1 shows the evolution of the acceleration measured at the ankle over time. It can be observed that, depending on the successive series performed by the participant, the ENMO amplitudes vary noticeably. The first series shows higher intensity peaks, while series 2 and 3 display a progressive decrease in the amplitude and variability of the signal, indicating a loss of explosiveness and an overall less intense movement.

<table>
  <tr>
    <th>Series1</th>
    <th>Series2</th>
    <th>Series3</th>
  </tr>
  <tr>
    <td>
      <img src="../resultats/ankle_Series1_trial2_ENMO_Trial2.png"
           alt="ankle_Series1_trial2_ENMO_Trial2" />
    </td>
    <td>
      <img src="../resultats/ankle_Series2_trial2_ENMO_Trial2.png"
           alt="ankle_Series2_trial2_ENMO_Trial2" />
    </td>
    <td>
      <img src="../resultats/ankle_Series3_trial2_ENMO_Trial2.png"
           alt="ankle_Series3_trial2_ENMO_Trial2" />
    </td>
  </tr>
</table>

**Figure 1: ENMO signal measured at the ankle for Series 1, Series 2 and Series 3.**

Regarding the sensor placed on the wrist (Figure 2), it can be noted that the explosiveness of the movement is generally maintained: the ENMO amplitudes remain almost identical between series 1 and series 3, with generally low values for all series. However, a slight decrease in intensity appears over time, indicating a moderate reduction in the amplitude of the wrist movement.

<table>
  <tr>
    <th>Series1</th>
    <th>Series2</th>
    <th>Series3</th>
  </tr>
  <tr>
    <td>
      <img src="../resultats/wrist_Series1_trial2_ENMO_Trial2.png"
           alt="wrist_Series1_trial2_ENMO_Trial2" />
    </td>
    <td>
      <img src="../resultats/wrist_Series2_trial2_ENMO_Trial2.png"
           alt="wrist_Series2_trial2_ENMO_Trial2" />
    </td>
    <td>
      <img src="../resultats/wrist_Series3_trial2_ENMO_Trial2.png"
           alt="wrist_Series3_trial2_ENMO_Trial2" />
    </td>
  </tr>
</table>

**Figure 2: ENMO signal measured at the wrist for Series 1, Series 2 and Series 3.**


### 4-2- Integrated ENMO analysis: fixed-window and sliding-window approaches

   Next, we examined each series using integrated ENMO with both fixed and sliding windows. The main results are summarised below. 

Figure 3 shows the curves obtained for series 1 with the sensor placed on the ankle. Figures 3a, 3b, and 3c correspond to the integrated ENMO using fixed windows, allowing the observation of the overall evolution of intensity during the exercise. Moving down one row in the table, Figures 3d, 3e, and 3f show the ENMO with sliding windows, which highlights finer variations and details of the signal. From this, it can be seen that integrating the ENMO clearly reveals the evolution of intensity throughout the exercise in each series. With a 10-second window, the signal shows rapid variations, marked by increases followed by abrupt decreases. With 20 seconds, these fluctuations are reduced, providing an averaged view of the effort. Finally, with 30 seconds, the signal becomes more stable, revealing mainly the overall trend without fine variations.

<table>
  <tr>
    <th>Integrated ENMO over 10s</th>
    <th>Integrated ENMO over 20s</th>
    <th>Integrated ENMO over 30s</th>
  </tr>

  <!-- Ligne 1 : fenêtres fixes -->
  <tr>
    <td>
      <div><strong>(a)</strong></div>
      <img src="../resultats/ankle_Series1_trial2_ENMO10s_fixed_Trial2.png"
           alt="ankle_Series1_trial2_ENMO10s_fixed_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
    <td>
      <div><strong>(b)</strong></div>
      <img src="../resultats/ankle_Series1_trial2_ENMO20s_fixed_Trial2.png"
           alt="ankle_Series1_trial2_ENMO20s_fixed_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
    <td>
      <div><strong>(c)</strong></div>
      <img src="../resultats/ankle_Series1_trial2_ENMO30s_fixed_Trial2.png"
           alt="ankle_Series1_trial2_ENMO30s_fixed_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
  </tr>

  <!-- Ligne 2 : fenêtres rolling -->
  <tr>
    <td>
      <div><strong>(d)</strong></div>
      <img src="../resultats/ankle_Series1_trial2_ENMO10s_rolling_Trial2.png"
           alt="ankle_Series1_trial2_ENMO10s_rolling_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
    <td>
      <div><strong>(e)</strong></div>
      <img src="../resultats/ankle_Series1_trial2_ENMO20s_rolling_Trial2.png"
           alt="ankle_Series1_trial2_ENMO20s_rolling_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
    <td>
      <div><strong>(f)</strong></div>
      <img src="../resultats/ankle_Series1_trial2_ENMO30s_rolling_Trial2.png"
           alt="ankle_Series1_trial2_ENMO30s_rolling_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
  </tr>
</table>

**Figure 3: Fixed-window (a–c) and sliding-window (d–f) integrated ENMO over 10, 20 and 30 s (ankle, Series 1).**

Figure 4 presents the same analyses as for the ankle (Figure 3), this time applied to Series 1 recorded at the wrist.

<table>
  <tr>
    <th>Integrated ENMO over 10s</th>
    <th>Integrated ENMO over 20s</th>
    <th>Integrated ENMO over 30s</th>
  </tr>

  <!-- Ligne 1 : fenêtres fixes -->
  <tr>
    <td>
      <div><strong>(a)</strong></div>
      <img src="../resultats/wrist_Series1_trial2_ENMO10s_fixed_Trial2.png"
           alt="wrist_Series1_trial2_ENMO10s_fixed_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
    <td>
      <div><strong>(b)</strong></div>
      <img src="../resultats/wrist_Series1_trial2_ENMO20s_fixed_Trial2.png"
           alt="wrist_Series1_trial2_ENMO20s_fixed_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
    <td>
      <div><strong>(c)</strong></div>
      <img src="../resultats/wrist_Series1_trial2_ENMO30s_fixed_Trial2.png"
           alt="wrist_Series1_trial2_ENMO30s_fixed_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
  </tr>

  <!-- Ligne 2 : fenêtres rolling -->
  <tr>
    <td>
      <div><strong>(d)</strong></div>
      <img src="../resultats/wrist_Series1_trial2_ENMO10s_rolling_Trial2.png"
           alt="wrist_Series1_trial2_ENMO10s_rolling_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
    <td>
      <div><strong>(e)</strong></div>
      <img src="../resultats/wrist_Series1_trial2_ENMO20s_rolling_Trial2.png"
           alt="wrist_Series1_trial2_ENMO20s_rolling_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
    <td>
      <div><strong>(f)</strong></div>
      <img src="../resultats/wrist_Series1_trial2_ENMO30s_rolling_Trial2.png"
           alt="wrist_Series1_trial2_ENMO30s_rolling_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
  </tr>
</table>

**Figure 4: Sliding-window and fixed-window integrated ENMO over 10s,20,30s  (wrist, series 1).**

These graphs confirm that, for fatigue assessment, the integrated ENMO with a fixed 30-second window provides a stable and reproducible measure. Thus, a visualization of the evolution across series 1, 2, and 3 integrated with a 30-second window is presented in Figure 5 below.

<table>
  <tr>
    <th></th>
    <th>Series1</th>
    <th>Series2</th>
    <th>Series3</th>
  </tr>

  <!-- Row 1: ankle -->
  <tr>
    <td><strong>Ankle</strong></td>
    <td>
      <div><strong>(a)</strong></div>
      <img src="../resultats/ankle_Series1_trial2_ENMO30s_fixed_Trial2.png"
           alt="ankle_Series1_trial2_ENMO30s_fixed_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
    <td>
      <div><strong>(b)</strong></div>
      <img src="../resultats/ankle_Series2_trial2_ENMO30s_fixed_Trial2.png"
           alt="ankle_Series2_trial2_ENMO30s_fixed_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
    <td>
      <div><strong>(c)</strong></div>
      <img src="../resultats/ankle_Series3_trial2_ENMO30s_fixed_Trial2.png"
           alt="ankle_Series3_trial2_ENMO30s_fixed_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
  </tr>

  <!-- Row 2: wrist -->
  <tr>
    <td><strong>Wrist</strong></td>
    <td>
      <div><strong>(d)</strong></div>
      <img src="../resultats/wrist_Series1_trial2_ENMO30s_fixed_Trial2.png"
           alt="wrist_Series1_trial2_ENMO30s_fixed_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
    <td>
      <div><strong>(e)</strong></div>
      <img src="../resultats/wrist_Series2_trial2_ENMO30s_fixed_Trial2.png"
           alt="wrist_Series2_trial2_ENMO30s_fixed_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
    <td>
      <div><strong>(f)</strong></div>
      <img src="../resultats/wrist_Series3_trial2_ENMO30s_fixed_Trial2.png"
           alt="wrist_Series3_trial2_ENMO30s_fixed_Trial2"
           style="max-width: 100%; height: auto;" />
    </td>
  </tr>
</table>

**Figure 5: Comparison of Ankle and Wrist Signals Across Series 1, 2 and 3 Using 30-s Fixed Integrated ENMO**

**Series 1 (5a and 5b), Ankle–Wrist Comparison:** 
The sensor placed on the ankle (5a) shows a very pronounced dynamic. The intensity increases progressively until reaching a peak of about 30 g·s around 100 seconds. Immediately after this maximum, the integrated ENMO drops sharply, with a rapid decrease until reaching a value close to 0 g·s around 160 seconds. This clear decline reflects a significant and rapid loss of explosiveness in the lower limbs. At the wrist (5b), the same series shows a much lower amplitude. The maximum intensity, about 14 g·s, appears earlier, between 80 and 90 seconds. The subsequent decrease is much more gradual, and the ENMO remains around 10 g·s at 140 seconds. This shows that wrist movement remains relatively stable and less affected by muscle fatigue.

**Series 2 (5c and 5d), Ankle–Wrist Comparison:** 
The ankle (5c) shows an overall lower intensity than in series 1. The activity peak reaches about 3.5 g·s around 45 seconds, followed by a regular decrease down to about 0.5 g·s at 100 seconds. The curve shows a less explosive dynamic and a more moderate loss of intensity, indicating fatigue already present at the beginning of this series. At the wrist (5d), the peak is around 2.6 g·s between 40 and 45 seconds, with a gradual decrease reaching about 2 g·s at the end of the series. As in series 1, the decline is smooth and regular, again highlighting that the wrist only indirectly reflects lower-limb fatigue.

**Series 3 (5e and 5f), Ankle–Wrist Comparison:** 
For series 3, the ankle (5e) shows an even more characteristic fatigue curve. The initial intensity is low, around 2.3 g·s at 15 seconds, and decreases continuously to about 0.2 g·s at 45 seconds. The trend is clearly linear and downward, showing an almost complete absence of explosiveness in jump propulsion. In contrast, the wrist (5f) shows a clear increase from the initial point toward the 45-second mark, after which the curve stabilizes around 13–15 g·s. 

These initial results indicate that the sensor placed on the ankle clearly reflects the onset of fatigue, while the wrist remains almost constant. Indeed, the ENMO variations at the ankle show a progressive, and sometimes abrupt,  decrease in intensity across the series, which directly reflects the loss of explosiveness in the lower limbs. In contrast, the wrist displays lower amplitudes and a much more stable evolution, mainly reflecting the regular rotation of the rope, a movement less influenced by muscular fatigue. Thus, the ankle appears to be the most relevant location for characterizing fatigue during a jump rope exercise.

### 4-3- Boxplot comparison of series 1–3 between ankle and wrist
These three graphs show, for Series 1, 2 and 3 of Trial 2, a comparison of the movements measured at the ankle and at the wrist using boxplots. For each series, the left panel displays the distribution of ENMO values (movement intensity) for both sensor locations, and the right panel shows the distribution of MAD values (signal variability). The boxplots summarize the entire recording: they indicate the overall activity level (position of the median), the spread of values over time (height of the box and length of the whiskers), and the presence of particularly marked movement episodes (extreme points).
These figures therefore make it possible to visualise how movement intensity and variability are distributed between the ankle and the wrist for each series.

![Series 1 – trial 2 ankle vs wrist](../resultats/Series1_trial2_ankle_vs_wrist.png)

**Figure 6: Comparison of ENMO and MAD distributions between the ankle and the wrist in Series 1**

In Series 1, the graphs show ENMO levels (Figure 6) that are overall similar at the ankle and the wrist, suggesting a comparable average movement intensity at both locations. However, the upper part of the ankle boxplot extends higher and contains more extreme values, indicating that the most intense episodes of the trial (sudden movements, impacts, rapid accelerations) occur more frequently or more markedly at the ankle. For MAD, a slightly greater spread is also observed at the ankle, reflecting a signal that is somewhat more unstable and variable over time than at the wrist. In this first condition, the lower limb therefore appears to be slightly more solicited than the upper limb, while the overall activity profile remains relatively balanced between the two sensors.

![Series 2 – trial 2 ankle vs wrist](../resultats/Series2_trial2_ankle_vs_wrist.png)

**Figure 7: Comparison of ENMO and MAD distributions between the ankle and the wrist in Series 2**

In Series 2 (Figure 7), the difference between ankle and wrist is more pronounced than in Series 1. In the ENMO boxplots, the medians are still relatively close, but the ankle box is slightly shifted towards higher values and, more importantly, the ankle shows a much taller column of extreme points than the wrist. This indicates that, even if the average movement intensity is comparable, the most intense movement episodes occur more frequently and more markedly at the ankle. A similar pattern appears for MAD: both the median and the spread are higher for the ankle, with more extreme values than at the wrist. This reflects greater variability in the ankle signal, meaning that accelerations are both stronger and more irregular over time. This profile is consistent with a situation in which the legs produce most of the mechanical work (for example during fast locomotion or frequent changes of pace), while the wrist mainly follows the movement and remains less heavily loaded.

![Series 3 – trial 2 ankle vs wrist](../resultats/Series3_trial2_ankle_vs_wrist.png)

**Figure 8: Comparison of ENMO and MAD distributions between the ankle and the wrist in Series 3**

In contrast with the previous series, in Series 3 the pattern clearly shifts in favour of the wrist. In the ENMO boxplots (Figure 8), wrist values are higher: the median is clearly above that of the ankle, the box is wider, and the column of extreme points extends to much larger values. The ankle, by contrast, remains concentrated around low ENMO values, with few very intense episodes. MAD shows a similar pattern: both the spread and the number of extreme values are greater at the wrist, whereas the ankle displays a more compact distribution centred on low to moderate levels. Taken together, these results suggest that in this condition the strongest and most irregular movements are mainly produced by the upper limb (arm swings, manipulations, trunk movements driving the wrist), while the lower limbs remain relatively stable or follow a more regular movement pattern.

Overall, the three figures show that the relative contribution of the ankle and the wrist to the measured activity varies across series. In Series 1 and 2, ENMO and MAD values are higher at the ankle, indicating a predominance of lower-limb movements. In contrast, in Series 3 these indices are higher at the wrist, reflecting a greater involvement of the upper limb in the activity.

### 5- Discussion

The approach chosen in this study, using accelerometers to monitor muscle fatigue during a repetitive exercise such as jump rope, is consistent with the methods currently described in the biomechanics and movement science literature. Several studies have shown that fatigue in the lower limb muscles (particularly the triceps surae and quadriceps) causes specific changes in the acceleration signals recorded in the leg during tasks such as jumping or running. For example, Sandrey et al. studied the effect of fatigue on leg muscle activation and tibial acceleration during a jumping task and reported significant changes in acceleration peaks and impact profiles between the pre-fatigue and post-fatigue conditions (Sandrey et al., 2020). Similarly, Flynn et al. showed that localized fatigue of the leg muscles alters shock transmission at the tibia during repeated ballistic activities, confirming that accelerometers placed near the ankle or tibia are sensitive to the effects of muscle fatigue (Flynn et al., 2004).

Beyond these experimental studies, a recent systematic review devoted to identifying lower limb fatigue using accelerometry concludes that parameters derived from tibial and sacral accelerations (particularly acceleration peaks and certain measures of variability) are the most frequently used and that they change significantly with fatigue during cyclic exercises such as running or jumping (Marotta et al., 2022). These results support the idea that accelerometry is a relevant method for monitoring the progressive deterioration of muscle performance during repetitive exercise.

The issue of sensor placement is also documented. Cabarkapa et al. showed that the anatomical position of the accelerometer strongly influences the biomechanical characteristics measured during a counter-movement jump, particularly variables related to the push-off and landing phases (CABARKAPA et al., 2022). Their results indicate that sensors located on segments directly involved in force production (lower limbs) are better at capturing performance variations than those placed on more distal or less stressed segments. These observations support the logic of comparing, in the present study, a sensor located at the ankle – close to the muscle groups responsible for propulsion and stabilization during rope jumping – with a sensor placed at the wrist, whose role is more related to the rotation of the rope than to the production of force on the ground.

In addition, the use of ENMO and MAD as metrics is supported by large-scale studies such as the German National Cohort (NAKO, >70,000 participants), where these acceleration-based indices have been validated as robust and reproducible measures of movement intensity. Although NAKO focused on physical activity rather than fatigue, their findings reinforce the appropriateness of ENMO and MAD for capturing meaningful variations in movement patterns in large populations, demonstrating that these metrics are widely accepted and reliable for biomechanical assessments.

Previous studies show that:
* muscle fatigue in the lower limbs results in measurable changes in leg accelerations (Sandrey et al., 2020);
* sensors placed on segments involved in propulsion (tibia, ankle) are more sensitive to these effects than those located on the upper limbs (CABARKAPA et al., 2022);
* metrics derived from the acceleration norm, such as ENMO, are recognized as useful for quantifying the intensity and variation of movement during physical exercise (Bakrania et al., 2016).

Thus, even without looking at the detailed results, all of these references confirm that the protocol used in this study is based on sound methodological choices and is in line with the current state of knowledge on the use of accelerometry to study muscle fatigue. In the present experiment, our results are consistent with these findings. At the ankle, ENMO and MAD clearly decrease across the three series and the highest values become rarer, which is compatible with a progressive loss of lower-limb power during the jump rope task. At the wrist, by contrast, ENMO and MAD remain more stable and generally lower in Series 1 and 2, indicating that this sensor mainly reflects rope rotation rather than the decline in leg performance. Only in Series 3 do the wrist values become relatively higher, not because the upper limb is more fatigued, but because ankle propulsion has dropped so much that wrist movements dominate the remaining signal. Overall, this supports the idea that a sensor placed close to the propulsive segments (ankle) is more sensitive to fatigue than one placed on the upper limb (wrist) (Weber et al., 2024).

### 6- Conclusion

This study analyzed acceleration signals recorded simultaneously at the ankle and wrist during jump-rope exercise using ENMO and MAD. The results show a progressive decrease in movement intensity and variability at the ankle, consistent with the onset of lower-limb fatigue, whereas the wrist remains relatively stable, primarily reflecting task execution. Boxplot comparisons confirm that the most intense activity is initially dominated by the ankle and later by the wrist as leg propulsion declines.

These findings confirm that sensor placement is a key factor in detecting muscle fatigue. Ankle-mounted devices are particularly suitable for monitoring loss of lower-limb explosiveness, while wrist-mounted sensors provide complementary information on overall task movement. Despite the limitations of a single participant and a specific protocol, this study illustrates the potential of ENMO- and MAD-based accelerometry for tracking fatigue-related changes in movement and provides a solid foundation for future research involving larger samples and multimodal fatigue measures.


### 7- Bibliographie

Bakrania K, Yates T, Rowlands AV, Esliger DW, Bunnewell S, Sanders J, Davies M, Khunti K, Edwardson CL (2016) Intensity Thresholds on Raw Acceleration Data: Euclidean Norm Minus One (ENMO) and Mean Amplitude Deviation (MAD) Approaches. PLoS One 11:e0164045. 

CABARKAPA DV, FRY AC, CABARKAPA D, PARRA ME, HERMES MJ (2022) Impact of accelerometer placement on assessment of vertical jump performance  parameters. JPES 22. 

Flynn JM, Holmes JD, Andrews DM (2004) The effect of localized leg muscle fatigue on tibial impact acceleration. Clinical Biomechanics 19:726–732. 

Marotta L, Scheltinga BL, Middelaar R van, Bramer WM, Beijnum B-JF van, Reenalda J, Buurke JH, Marotta L, Scheltinga BL, Middelaar R van, Bramer WM, Beijnum B-JF van, Reenalda J, Buurke JH (2022) Accelerometer-Based Identification of Fatigue in the Lower Limbs during Cyclical Physical Exercise: A Systematic Review. Sensors 22 Available at: https://www.mdpi.com/1424-8220/22/8/3008 [Accessed November 29, 2025]. 

Sandrey MA, Chang Y-J, McCrory JL (2020) The Effect of Fatigue on Leg Muscle Activation and Tibial Acceleration During a Jumping Task. Journal of Sport Rehabilitation 29:1093–1099. 

Weber A et al. (2024) Large-scale assessment of physical activity in a population using high-resolution hip-worn accelerometry: the German National Cohort (NAKO). Sci Rep 14:7927. 

(PDF) Large-scale assessment of physical activity in a population using high-resolution hip-worn accelerometry: the German National Cohort (NAKO)Weber A et al. (2024) Large-scale assessment of physical activity in a population using high-resolution hip-worn accelerometry: the German National Cohort (NAKO). Sci Rep 14:7927. 








