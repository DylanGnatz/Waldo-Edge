import { Storage } from "aws-amplify";

export async function s3Upload(file, personID, personName, phoneNumber) {
  personName = personName.replace(" ", "_");
  const filename = `${personID}_${personName}_${phoneNumber}`;

  const stored = await Storage.vault.put(filename, file, {
    contentType: file.type
  });

  return stored.key;
}
