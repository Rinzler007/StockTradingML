def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9999
   if obj[3] == 'Sell':
      # Feature: SMA2, Instances: 74, Entropy: 0.9809
      if obj[5] == 'Sell':
         # Feature: SMA1, Instances: 46, Entropy: 0.9109
         if obj[4] == 'Buy':
            # Feature: MACD, Instances: 24, Entropy: 0.8113
            if obj[2] == 'Sell':
               # Feature: RSI, Instances: 18, Entropy: 0.65
               if obj[1] == 'Hold':
                  # Feature: Closing, Instances: 17, Entropy: 0.6723
                  if obj[0]<=75.961998:
                     return 'No'
                  elif obj[0]>75.961998:
                     return 'No'
                  else:
                     return 'No'
               elif obj[1] == 'Buy':
                  return 'No'
               else:
                  return 'No'
            elif obj[2] == 'Buy':
               # Feature: Closing, Instances: 6, Entropy: 1.0
               if obj[0]<=75.961998:
                  # Feature: RSI, Instances: 4, Entropy: 1.0
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               elif obj[0]>75.961998:
                  # Feature: RSI, Instances: 2, Entropy: 1.0
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[4] == 'Sell':
            # Feature: Closing, Instances: 22, Entropy: 0.976
            if obj[0]<=75.961998:
               # Feature: MACD, Instances: 19, Entropy: 0.9495
               if obj[2] == 'Buy':
                  # Feature: RSI, Instances: 11, Entropy: 0.9457
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Sell':
                  # Feature: RSI, Instances: 8, Entropy: 0.9544
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[0]>75.961998:
               # Feature: MACD, Instances: 3, Entropy: 0.9183
               if obj[2] == 'Buy':
                  # Feature: RSI, Instances: 2, Entropy: 1.0
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         else:
            return 'No'
      elif obj[5] == 'Buy':
         # Feature: Closing, Instances: 28, Entropy: 0.9852
         if obj[0]<=75.961998:
            # Feature: SMA1, Instances: 20, Entropy: 0.9928
            if obj[4] == 'Buy':
               # Feature: MACD, Instances: 16, Entropy: 0.9544
               if obj[2] == 'Sell':
                  # Feature: RSI, Instances: 14, Entropy: 0.9403
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Buy':
                  # Feature: RSI, Instances: 2, Entropy: 1.0
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Sell':
               # Feature: MACD, Instances: 4, Entropy: 0.8113
               if obj[2] == 'Buy':
                  # Feature: RSI, Instances: 3, Entropy: 0.9183
                  if obj[1] == 'Hold':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[0]>75.961998:
            # Feature: RSI, Instances: 8, Entropy: 0.5436
            if obj[1] == 'Hold':
               return 'Yes'
            elif obj[1] == 'Buy':
               return 'No'
            else:
               return 'No'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Hold':
      # Feature: RSI, Instances: 33, Entropy: 0.7455
      if obj[1] == 'Sell':
         # Feature: Closing, Instances: 18, Entropy: 0.5033
         if obj[0]<=75.961998:
            # Feature: SMA1, Instances: 11, Entropy: 0.684
            if obj[4] == 'Buy':
               # Feature: MACD, Instances: 8, Entropy: 0.5436
               if obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 8, Entropy: 0.5436
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[4] == 'Sell':
               # Feature: MACD, Instances: 3, Entropy: 0.9183
               if obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 3, Entropy: 0.9183
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[0]>75.961998:
            return 'Yes'
         else:
            return 'Yes'
      elif obj[1] == 'Hold':
         # Feature: Closing, Instances: 15, Entropy: 0.9183
         if obj[0]<=75.961998:
            # Feature: MACD, Instances: 11, Entropy: 0.9457
            if obj[2] == 'Buy':
               # Feature: SMA2, Instances: 9, Entropy: 0.9183
               if obj[5] == 'Buy':
                  # Feature: SMA1, Instances: 7, Entropy: 0.8631
                  if obj[4] == 'Buy':
                     return 'Yes'
                  elif obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Sell':
                  # Feature: SMA1, Instances: 2, Entropy: 1.0
                  if obj[4] == 'Sell':
                     return 'Yes'
                  elif obj[4] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[2] == 'Sell':
               # Feature: SMA1, Instances: 2, Entropy: 1.0
               if obj[4] == 'Buy':
                  # Feature: SMA2, Instances: 2, Entropy: 1.0
                  if obj[5] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[0]>75.961998:
            # Feature: SMA2, Instances: 4, Entropy: 0.8113
            if obj[5] == 'Sell':
               return 'Yes'
            elif obj[5] == 'Buy':
               # Feature: MACD, Instances: 2, Entropy: 1.0
               if obj[2] == 'Sell':
                  return 'Yes'
               elif obj[2] == 'Buy':
                  return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      return 'No'
   else:
      return 'No'
