# Module 27. Computer Systems Management

The exam treats the planning system as a clinical device: archives, backups, updates, and scripts. The vocabulary is simple. The failure mode is a plan that cannot be restored, or a script that applied the wrong rule to every patient.

## Comp-Sci Terms (Simplified)

**MDCB objectives:** III.9

**What the exam expects**

You can define the words a dosimetrist needs in a chart-check or a downtime conversation: bit, byte, file, server, database, pixel, voxel, algorithm, script, backup, archive. You can do a one-line binary count so “8 bits” means something. Full binary-to-decimal drills belong to the bonus calculation set. This lesson is the vocabulary those drills assume.

**Core facts**

A bit is one binary digit, 0 or 1. A byte is 8 bits. With 8 bits you can represent 2⁸ = 256 different values, from 0 through 255. That is why an old image pixel is often an 8-bit number, and why a Hounsfield unit, which spans a wider range than 0–255, needs more than 8 bits or a stored slope and intercept.

Three bits are enough to count the idea:

2³ = 8 values (0 through 7).

Four bits: 2⁴ = 16 values. Ten bits: 2¹⁰ = 1024, the old “kilobyte” of 1024 bytes. You will not be asked to design a computer. You may be asked what a byte is, or why a pixel value and a Hounsfield unit are not the same stored number until the rescale slope is applied.

A pixel is one picture element on a 2D image. A voxel is the 3D cell: pixel spacing times pixel spacing times slice spacing. Dose grids and CT grids are both voxel arrays, and they are often different sizes. A DVH samples the dose voxels inside a contour. A coarse dose voxel hides a narrow hot spot. That limit is the uncertainty module’s topic; the word you need here is voxel.

An algorithm is a defined procedure that turns an input into an output: a dose engine, a registration, a leaf sequencer. A script is an algorithm written down so the computer can repeat it: rename structures, set a course of objectives, export a DVH. A template is a stored starting point. A script that calls the wrong template is still “working.”

A file is a named block of bytes. A database is an organized set of records the oncology information system can query: patients, courses, documents. A server is a computer that holds those files or that database and answers other computers. A PACS holds images. The planning system holds plans and doses. The record-and-verify system holds what the machine will deliver. DICOM is the usual language between them (module 26).

RAM is working memory and is cleared when the process ends. Disk or solid-state storage keeps the plan after you log out. A plan that exists only in an unsaved session does not exist in the archive.

A network moves the bytes. Bandwidth limits how fast a CT series travels. A firewall and an application entity title decide whether a DICOM node is allowed to talk. “The file is on a shared drive” and “the file was accepted by the planning DICOM node” are different events.

**Formulas**

Values representable by n bits:

N = 2ⁿ

Eight bits: N = 2⁸ = 256.

A CT matrix of 512 × 512 pixels per slice, and 200 slices, is

512 × 512 × 200 = 52,428,800 voxels

of image data, before you count the bytes per voxel. If each voxel is stored in 2 bytes,

52,428,800 × 2 = 104,857,600 bytes ≈ 100 megabytes

for that series, ignoring headers. A dose grid at a different spacing is a different count. The point of the arithmetic is that image storage is finite, and a full course with four-dimensional phases, multiple plans, and daily cone-beams is much larger than one slice.

**Traps**

- Calling a byte a bit. A byte is 8 bits.
- Assuming 512 × 512 × 2 bytes is the whole chart. Cone-beams and multiple plans dominate the archive.
- Treating a script and a commissioned algorithm as the same kind of “checked.” The dose engine was commissioned. The script someone wrote last week may not have been.
- Confusing pixel value with Hounsfield number when a rescale slope is present.

**Sources**

- DICOM image modules, for bits stored, rescale slope, and pixel spacing
- The TPS administrator’s description of what is actually archived in your department

## Computer Systems Management

**MDCB objectives:** III.9, III.10

**What the exam expects**

You can separate a backup from an archive, say why RAID is not a backup, and say what has to happen before a dose-engine upgrade is used on a patient. You can explain how a script scales both a good habit and a bad one. Routine maintenance is a clinical safety task, not only an IT task.

**Core facts**

An archive is the long-term record: the plan, the dose, the structures, the documents, kept so the case can be reviewed or re-treated years later. A backup is a restorable copy made so a failure tomorrow does not destroy that record. They answer different questions. An archive that lives on one disk and has no backup is a single point of failure. A backup that was never restored in a drill is a hope. The test of a backup is a restore, onto a system that can read the versions you actually use.

RAID mirrors or stripes disks so one disk can die without taking the file with it. It does not protect you from a delete, a bad script, or ransomware. The mirrored disk deletes the file too, faithfully. A backup is a separate copy, preferably offline or otherwise not writable by the same mistake. Confirm the retention time in the departmental policy. Do not invent a legal retention period on the exam unless the stem quotes one.

Routine maintenance that touches dose or geometry is commissioning work:

- A new build of the dose algorithm, a new CT density table, or a new linac beam model needs physics validation before clinical use.
- Operating-system patches that do not change the dose engine still need a sanity check that the system launches, licenses, and reads a known plan.
- Disks fill up. A full database fails a save in the middle of a transfer. Monitoring free space is part of keeping plans intact.
- Clocks, user accounts, and permissions decide who can approve a plan and whether the time stamp in the record is true.
- Downtime procedure: where treatment information lives if the oncology information system is down, and who may treat from a verified printed or local copy. That procedure is local. Know that it must exist.

Scripting and templates sit in the blueprint next to automated planning. A script may build beams, apply a naming convention, or pull DVH numbers for a chart check. Validate it on a phantom or a test patient, version it, and keep the version that ran with the plan. A script that mislabels left and right, or that sets 6 Gy where the template author meant 1.8 Gy, will do so on every case it touches. The review you would give a human planner still applies to the script’s output. Autoplanning judgment is the next module. The computer-system duty is change control: who may edit the script, and how a bad version is rolled back.

Security is part of management. Unique logins, a screen lock, and an audit trail keep the record attributable. Shared passwords make a later investigation impossible. Export to a laptop or a USB drive is a privacy event and a version-control event. The copy on the laptop is not the archive.

When a plan will not open after an upgrade, the rollback path is the previous software version plus the backup taken before the upgrade. Taking that backup is part of the upgrade, not an optional courtesy.

**Formulas**

Storage arithmetic from the previous lesson is the quantitative piece. One more clinical ratio: if daily cone-beams are 80 MB each and a 30-fraction course stores every one,

30 × 80 MB = 2400 MB ≈ 2.4 GB

per course, plus the planning CT and every adapted plan. Multiply by the number of patients under treatment and the archive policy becomes a capacity plan. The 80 MB figure is an illustration of the multiplication, not a measured size for your scanner. Use the size your system reports when you are actually sizing a disk.

**Traps**

- Calling RAID a backup.
- Upgrading the dose engine over a weekend and treating on Monday without a physics check.
- Editing a clinical script on the production system with no version and no test patient.
- Assuming the record-and-verify database and the planning database are one archive. Back up the one that can actually restore the case you will need.
- Deleting the primary after “it was exported somewhere.”

**Sources**

- Departmental backup, archive, and downtime policies. Confirm retention and the restore drill there.
- AAPM guidance on treatment-planning commissioning, for what must be rechecked when the software that calculates dose changes. Confirm the checklist in the report your clinic adopted (TG-53 is the classic TPS commissioning and QA report).
- DICOM and the oncology information system vendor documents, for what an export actually contains

## Computers Mini-Quiz

**MDCB objectives:** III.9

**Skills this quiz trains**

- Define bit, byte, pixel, voxel, script, backup, and archive.
- Compute 2⁸ = 256 and a simple voxel count.
- Explain why RAID does not survive a bad delete.
- Require a physics check when the dose algorithm changes.
- Require a version and a test run for a script that touches plans.

**Traps**

- Backup and archive used as synonyms.
- A script treated as inherently safer than a manual plan.
- Pixel value used as Hounsfield units with no rescale.
- A full disk treated as an IT annoyance rather than a failed save of a clinical plan.

**Check yourself**

How many distinct values can one byte hold? A mirrored disk pair both contain the planning database, and a script deletes last year’s courses from the database. Are those courses on the mirror?

Walk-through: A byte holds 2⁸ = 256 values. The mirror has the same deletion. Recovery depends on a backup taken before the script ran, not on RAID.
